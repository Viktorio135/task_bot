import json
import logging
import subprocess
import os
import dill as pickle

from dotenv import load_dotenv

load_dotenv()

user_bd = os.getenv('USER_BD')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')




async def dump_dicts(cached_data, main_menu_icon, tasks_progress, archive_tasks_progerss, warnings):
    try:
        with open('backups/cached_data.pkl', 'wb') as file:
            pickle.dump(cached_data, file)
        with open('backups/main_menu_icon.pkl', 'wb') as file:
            pickle.dump(main_menu_icon, file)
        with open('backups/tasks_progress.pkl', 'wb') as file:
            pickle.dump(tasks_progress, file)
        with open('backups/archive_tasks_progerss.pkl', 'wb') as file:
            pickle.dump(archive_tasks_progerss, file)
        with open('backups/warnings.pkl', 'wb') as file:
            pickle.dump(warnings, file)
        logging.info('Dump dicts')
        return 1
    except Exception as e:
        logging.error(f'Ошибка дампа dicts: {e}')
        return 0






async def backup_bd():
    try:
        backup_path = 'backups/database.sql'
        os.environ['MYSQL_PWD'] = password
        subprocess.run(['mysqldump', '-u', user_bd, database, '--result-file', backup_path])
        logging.info('Dump database')
    except Exception as e:
        logging.error(f'Ошибка дамба базы данных: {e}')
    finally:
        del os.environ['MYSQL_PWD']
