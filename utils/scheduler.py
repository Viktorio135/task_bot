from utils.dump import dump_dicts, backup_bd
from utils.time_manager import time_manage, delete_old_files, checking_done_tasks


def start_schedule(scheduler, cached_data, main_menu_icon, tasks_progress, archive_tasks_progerss, warnings):
    scheduler.add_job(dump_dicts, 'interval', minutes=10, args=(cached_data, main_menu_icon, tasks_progress, archive_tasks_progerss, warnings))
    scheduler.add_job(backup_bd, 'interval', minutes=60)
    scheduler.add_job(time_manage, 'interval', minutes=1, args=(tasks_progress, ))
    scheduler.add_job(delete_old_files, 'interval', hours=2)
    scheduler.add_job(checking_done_tasks, 'interval', minutes=5, args=(tasks_progress, archive_tasks_progerss, ))
