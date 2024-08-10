from aiogram.types import (
    InlineKeyboardMarkup, 
    ReplyKeyboardMarkup, 
    InlineKeyboardButton, 
    KeyboardButton
)

from database.db_commands import *

def admin_main_kb():
    btn1 = InlineKeyboardButton(text='Новое задание', callback_data='admin_new_task')
    btn2 = InlineKeyboardButton(text='Все задания', callback_data='admin_task')
    btn3 = InlineKeyboardButton(text='Пользователи', callback_data='admin_users')
    btn4 = InlineKeyboardButton(text='Общая статистика', callback_data='admin_stat')
    btn5 = InlineKeyboardButton(text='Рассылка', callback_data='admin_message')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4).add(btn5)
    return keyboard

async def get_category_kb():
    categories = await get_category()
    keyboard = InlineKeyboardMarkup()
    if (len(categories) != 0):
        for cat in categories:
            btn = InlineKeyboardButton(text=cat.name, callback_data=f'new_task_cat:{cat.name}')
            keyboard.add(btn)
    else:
        btn = InlineKeyboardButton(text='Ни одной категории еще нет', callback_data='nothing')
        keyboard.add(btn)
    return keyboard


def new_task_conf():
    btn1 = InlineKeyboardButton(text='Всё верно', callback_data='new_task_send')
    btn2 = InlineKeyboardButton(text='<<', callback_data='new_task_cancel')
    keyboard = InlineKeyboardMarkup().add(btn2, btn1)
    return keyboard

def new_task_cancel():
    btn1 = InlineKeyboardButton(text='<<', callback_data='new_task_cancel')
    keyboard = InlineKeyboardMarkup().add(btn1)
    return keyboard

def admin_all_task_kb():
    btn1 = InlineKeyboardButton(text='Активные', callback_data='active_admin_task')
    btn2 = InlineKeyboardButton(text='Архив', callback_data='admin_archeve_task')
    keybaord = InlineKeyboardMarkup().add(btn1, btn2)
    return keybaord


async def admin_all_active_tasks_kb(page, cached_data):
    tasks = await get_all_tasks()
    total_pages = len(tasks) // 7 + 1
    keyboard = InlineKeyboardMarkup()

    start_idx = page * 7
    end_idx = start_idx + 7
    current_tasks = tasks[start_idx:end_idx]

    for task in current_tasks:
        limit = cached_data[task.id]['limit']
        checking = len(cached_data[task.id]['users']['checking'])
        done = len(cached_data[task.id]['users']['done'])
        btn = InlineKeyboardButton(text=f'Задание #{task.id} {done}/{limit} - {checking}', callback_data=f'admin_all_tasks:{task.id}')
        keyboard.add(btn)
    
    btn1 = InlineKeyboardButton(text='<', callback_data=f'admin_all_task_last:{page-1}')
    btn2 = InlineKeyboardButton(text='>', callback_data=f'admin_all_task_next:{page+1}')
    keyboard.add(btn1, btn2)

    return keyboard


async def admin_all_archive_tasks_kb(page):
    tasks = await get_all_archive_tasks()
    total_pages = len(tasks) // 7 + 1
    keyboard = InlineKeyboardMarkup()

    start_idx = page * 7
    end_idx = start_idx + 7
    current_tasks = tasks[start_idx:end_idx]

    for task in current_tasks:
        task_datas = await get_archive_task_datas(int(task.number_task))
        done = task_datas["done"]
        limit = task_datas["count_people"]
        if int(done) == int(limit):
            btn = InlineKeyboardButton(text=f'✅ Задание #{task.number_task} {done}/{limit}', callback_data=f'admin_all_archive_tasks:{task.number_task}')
            keyboard.add(btn)
        else:
            btn = InlineKeyboardButton(text=f'❌ Задание #{task.number_task} {done}/{limit}', callback_data=f'admin_all_archive_tasks:{task.number_task}')
            keyboard.add(btn)
    btn1 = InlineKeyboardButton(text='<', callback_data=f'admin_all_archive_tasks_last:{page-1}')
    btn2 = InlineKeyboardButton(text='>', callback_data=f'admin_all_archive_tasks_next:{page+1}')
    keyboard.add(btn1, btn2)

    return keyboard





def admin_show_full_task_kb(number_task):
    btn1 = InlineKeyboardButton(text='Редактировать', callback_data=f'show_full_task_edit:{number_task}')
    btn2 = InlineKeyboardButton(text='Удалить', callback_data=f'show_full_task_delete:{number_task}')
    btn3 = InlineKeyboardButton(text='Выполнения', callback_data=f'show_full_task_checking:{number_task}')
    btn4 = InlineKeyboardButton(text='<<', callback_data='show_full_task_back')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4)
    return keyboard

def admin_edit_task_text_conf_kb():
    btn1 = InlineKeyboardButton(text='Всё верно', callback_data='admin_edit_text_conf')
    btn2 = InlineKeyboardButton(text='<<', callback_data='admin_edit_text_back')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2)
    return keyboard


def admin_delete_task_conf_kb(number_task):
    btn1 = InlineKeyboardButton(text='Уверен', callback_data=f'admin_delete_conf:{number_task}')
    btn2 = InlineKeyboardButton(text='<<', callback_data=f'admin_delete_cancel')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
    return keyboard

def admin_checking_kb(number_task, user_id, place=0):
    btn1 = InlineKeyboardButton(text='Принять', callback_data=f'accept_admin__task:{number_task}:{user_id}:{place}')
    btn2 = InlineKeyboardButton(text='Отклонить', callback_data=f'reject_admin_task:{number_task}:{user_id}:{place}')
    btn3 = InlineKeyboardButton(text='<', callback_data=f'admin_last_checking:{number_task}:{place-1}')
    btn4 = InlineKeyboardButton(text='>', callback_data=f'admin_next_checking:{number_task}:{place+1}')
    keyboard = InlineKeyboardMarkup().add(btn3, btn4).add(btn1, btn2)
    return keyboard


def admin_reject_task_kb():
    btn1 = InlineKeyboardButton(text='<<', callback_data='admin_reject_task_cancel')
    keyboard = InlineKeyboardMarkup().add(btn1)
    return keyboard

def admin_all_task_archive_full_kb(number_task):
    btn1 = InlineKeyboardButton(text='Список выполнивших', callback_data=f'list_of_done:{number_task}')
    btn2 = InlineKeyboardButton(text='<<', callback_data='all_task_archive_full_back')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
    return keyboard

def admin_users_kb(user_id):
    btn1 = InlineKeyboardButton(text='Предупреждения', callback_data=f'admin_user_warning:{user_id}')
    btn2 = InlineKeyboardButton(text='Выдать баланс', callback_data=f'admin_user_adding_balance:{user_id}')
    btn3 = InlineKeyboardButton(text='Вычесть баланс', callback_data=f'admin_user_subtract_balance:{user_id}')
    btn4 = InlineKeyboardButton(text='Задания', callback_data=f'admin_show_user_tasks:{user_id}')
    btn5 = InlineKeyboardButton(text='<<', callback_data='admin_back_user')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3, btn4).add(btn5)
    return keyboard

def admin_users_warnings_kb(user_id):
    btn1 = InlineKeyboardButton(text='Предупреждение', callback_data=f'admin_adding_warning:{user_id}')
    btn2 = InlineKeyboardButton(text='Блокировка', callback_data=f'admin_block_user:{user_id}')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2)
    return keyboard

def admin_ublock_user_conf(user_id):
    btn1 = InlineKeyboardButton(text='Уверен', callback_data=f'admin_conf_block_user:{user_id}')
    btn2 = InlineKeyboardButton(text='Отмена', callback_data=f'admin_conf_calcel_block')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2)
    return keyboard

def admin_show_user_task_kb(user_id):
    btn1 = InlineKeyboardButton(text='Зачесть выполнение', callback_data=f'admin_give_done_task:{user_id}')
    btn2 = InlineKeyboardButton(text='Все задания', callback_data=f'admin_show_all_user_task:{user_id}')
    keyborad = InlineKeyboardMarkup().add(btn1, btn2)
    return keyborad