from database.db_commands import is_time_remaining, delete_active_task, adding_user_times, subtract_user_in_process, get_task_datas, adding_archive_task, delete_task, adding_stat_del_task
import os, datetime, shutil


async def time_manage(tasks_progress):
    for task in dict(tasks_progress):
        for user in dict(tasks_progress[task]['users']['in_process']):
            start_time = tasks_progress[task]['users']['in_process'][user]
            timer = tasks_progress[task]['timer']
            if timer != '00':
                remaining_time = await is_time_remaining(start_time=start_time, duration_minutes=timer)
                if remaining_time == 0:
                    tasks_progress[task]['users']['rejected'][user] = {
                        'reason': 'Лимит времени'
                    }
                    del tasks_progress[task]['users']['in_process'][user]
                    await delete_active_task(str(user), str(task))
                    await subtract_user_in_process(str(user))
                    await adding_user_times(str(user))


async def delete_old_files():
    now = datetime.datetime.now()
    # Определяем дату, которая была неделю назад
    week_ago = now - datetime.timedelta(days=7)

    # Проходим по всем подпапкам в указанной директории
    for root, dirs, files in os.walk('static/archive'):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            # Получаем время последнего изменения файла
            file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            # Если файл старше недели, удаляем его
            if file_time < week_ago:
                os.remove(file_path)

async def checking_done_tasks(tasks_progress, archive_tasks_progress):
    for task in dict(tasks_progress):
        limit = tasks_progress[task]["limit"]
        if len(tasks_progress[task]["users"]["done"]) >= int(limit):
            task_datas = await get_task_datas(task)
            cancelled = len(tasks_progress[task]['users']['canceled'])
            done = len(tasks_progress[task]['users']['done'])
            rejected = 0
            times = 0
            for user in tasks_progress[task]['users']['rejected']:
                if tasks_progress[task]['users']['rejected'][user]['reason'] != 'Лимит времени':
                    rejected += 1
                else:
                    times += 1
            await adding_archive_task(
                number_task=task_datas["id"],
                category=task_datas["category"],
                full_text=task_datas["full_text"],
                small_text=task_datas["small_text"],
                price=task_datas["price"],
                timer=task_datas["timer"],
                count_people=task_datas["count_people"],
                start_date=task_datas["start_date"],
                end_date=datetime.datetime.now(),
                who_created=task_datas["who_created"],
                rejected=rejected,
                cancelled=cancelled,
                times=times,
                done=done
            )
            await delete_task(task)
            await adding_stat_del_task()
            archive_tasks_progress[task] = tasks_progress[task]
            del tasks_progress[task]
            shutil.rmtree(f'static/tasks/{task}')
                