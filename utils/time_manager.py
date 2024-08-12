from database.db_commands import is_time_remaining, delete_active_task, adding_user_times, subtract_user_in_process
import os, datetime


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
                