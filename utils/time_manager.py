from database.db_commands import is_time_remaining, delete_active_task, adding_user_times, subtract_user_in_process



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