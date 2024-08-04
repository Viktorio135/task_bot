from utils.dump import dump_dicts, backup_bd
from utils.time_manager import time_manage


def start_schedule(scheduler, cached_data, main_menu_icon, tasks_progress):
    scheduler.add_job(dump_dicts, 'interval', minutes=10, args=(cached_data, main_menu_icon, tasks_progress, ))
    scheduler.add_job(backup_bd, 'interval', minutes=30)
    scheduler.add_job(time_manage, 'interval', minutes=1, args=(tasks_progress, ))
