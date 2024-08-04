from aiogram.types import (
    InlineKeyboardMarkup, 
    ReplyKeyboardMarkup, 
    InlineKeyboardButton, 
    KeyboardButton
)

from database.db_commands import *

def check_sub():
    btn1 = InlineKeyboardButton(text='Проверить', callback_data='check_sub')
    keyboard = InlineKeyboardMarkup().add(btn1)
    return keyboard

def reset_wallet():
    btn1 = InlineKeyboardButton(text='<<', callback_data='reser_wallet')
    keyboard = InlineKeyboardMarkup().add(btn1)
    return keyboard


def start_skip_wallet(start=True):
    btn1 = InlineKeyboardButton(text='Пропустить', callback_data='start_skip_wallet')
    btn2 = InlineKeyboardButton(text='Российский банк', callback_data='bank_wallet:rus')
    btn3 = InlineKeyboardButton(text='Украинский банк', callback_data='bank_wallet:ukr')
    btn4 = InlineKeyboardButton(text='Юмани', callback_data='bank_wallet:umoney')
    btn5 = InlineKeyboardButton(text='USDT-BEP20', callback_data='bank_wallet:usdt')
    if start:
        keyboard = InlineKeyboardMarkup().add(btn2, btn3).add(btn4, btn5).add(btn1)
    else:
        keyboard = InlineKeyboardMarkup().add(btn2, btn3).add(btn4, btn5)
    return keyboard

def start_wallet_skip_phone():
    btn1 = InlineKeyboardButton(text='Пропустить', callback_data='start_wallet_skip_phone')
    btn2 = InlineKeyboardButton(text='<<', callback_data='reser_wallet')
    keyboard = InlineKeyboardMarkup().add(btn2, btn1)
    return keyboard

def main_kb():
    btn1 = KeyboardButton(text='❗ Список заданий')
    btn2 = KeyboardButton(text='👤 Мой профиль')
    btn3 = KeyboardButton(text='🛟 Помощь')
    btn4 = KeyboardButton(text='🔎 Поиск задания')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(btn1, btn2).row(btn3, btn4)
    return keyboard

def inline_main_kb():
    btn1 = InlineKeyboardButton(text='💳 Кошелек', callback_data='wallet')
    btn2 = InlineKeyboardButton(text='📝 Мои выполнения', callback_data='my_menu_tasks')
    btn3 = InlineKeyboardButton(text='🔈 Уведомления', callback_data='notifications')
    btn4 = InlineKeyboardButton(text='🔗 мои соцсети', callback_data='contacts')
    keyboard = InlineKeyboardMarkup().add(btn1, btn3).add(btn2, btn4)
    return keyboard


def edit_wallet():
    btn1 = InlineKeyboardButton(text='✏️ Изменить', callback_data='edit_wallet')
    btn2 = InlineKeyboardButton(text='🗑️🗑️ Удалить', callback_data='delete_wallet')
    btn3 = InlineKeyboardButton(text='<<', callback_data='wallet_back')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3)
    return keyboard

def delete_wallet():
    btn1 = InlineKeyboardButton(text='<<', callback_data='delete_wallet_back')
    btn2 = InlineKeyboardButton(text='🗑️🗑️ Удалить', callback_data='delete_wallet_conf')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2)
    return keyboard


def support_kb():
    btn1 = InlineKeyboardButton(text='🤝 Сотрудничество', url='https://chat.deepseek.com/coder')
    btn2 = InlineKeyboardButton(text='ℹ️ FAQ', url='https://chat.deepseek.com/coder')
    btn3 = InlineKeyboardButton(text='💁‍♂️ Поддержка', url='https://chat.deepseek.com/coder')
    btn4 = InlineKeyboardButton(text='🚀 Новости', url='https://chat.deepseek.com/coder')
    btn5 = InlineKeyboardButton(text='ℹ️ Правила', url='https://chat.deepseek.com/coder')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn4, btn3).add(btn5)
    return keyboard

def notifications_kb(params):
    btn1 = InlineKeyboardButton(text=f'{"🔔" if params[0] == "1" else "🔕"} Новости бота', callback_data='change_notifications_news')
    btn2 = InlineKeyboardButton(text=f'{"🔔" if params[1] == "1" else "🔕"} Нововые задания', callback_data='change_notifications_tasks')
    btn3 = InlineKeyboardButton(text=f'{"🔔" if params[2] == "1" else "🔕"} Нововые оценки', callback_data='change_notifications_assessments')
    btn4 = InlineKeyboardButton(text='<<', callback_data='notifications_back')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2).add(btn3).add(btn4)
    return keyboard


def contacnts_no_acc():
    btn1 = InlineKeyboardButton(text=f'➕ Добавить YouTube', callback_data='adding_acc')
    btn2 = InlineKeyboardButton(text=f'<<', callback_data='contacts_back')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
    return keyboard

def contacts_kb():
    btn1 = InlineKeyboardButton(text=f'<<', callback_data='contacts_back')
    btn2 = InlineKeyboardButton(text=f'✏️ Изменить', callback_data='adding_acc')
    keyboard = InlineKeyboardMarkup().add(btn2).add(btn1)
    return keyboard



def adding_youtube():
    btn1 = InlineKeyboardButton(text=f'<<', callback_data='contacts_youtube_back')
    keyboard = InlineKeyboardMarkup().add(btn1)
    return keyboard



def accept_new_task(number):
    btn1 = InlineKeyboardButton(text='Принять', callback_data=f'accept_new_task:{number}')
    btn2 = InlineKeyboardButton(text='Отклонить', callback_data=f'reject_new_task:{number}')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2)
    return keyboard



async def get_all_category_kb():
    categories = await get_category()
    keyboard = InlineKeyboardMarkup()
    if (len(categories) != 0):
        for cat in categories:
            btn = InlineKeyboardButton(text=cat.name, callback_data=f'task_category:{cat.name}')
            keyboard.add(btn)
    else:
        btn = InlineKeyboardButton(text='Ни одной категории еще нет', callback_data='nothing')
        keyboard.add(btn)
    return keyboard

def next_task_kb(place,category, is_hand=False, task_number=0, checking=False):
    if checking:
        btn1 = InlineKeyboardButton(text='📎 На проверке', callback_data='nothing')
        btn2 = InlineKeyboardButton(text='<', callback_data=f'last_task:{place-1}:{category}')
        btn3 = InlineKeyboardButton(text='>', callback_data=f'next_task:{place+1}:{category}')
        btn4 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn2, btn3).add(btn4)
        return keyboard
    if is_hand:
        btn1 = InlineKeyboardButton(text='❎ Сдать', callback_data='hand')
        btn5 = InlineKeyboardButton(text='❌ Отказаться', callback_data=f'cancel_task:{task_number}')
        btn2 = InlineKeyboardButton(text='<', callback_data=f'last_task:{place-1}:{category}')
        btn3 = InlineKeyboardButton(text='>', callback_data=f'next_task:{place+1}:{category}')
        btn4 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn5).add(btn2, btn3).add(btn4)
        return keyboard
    else:
        btn1 = InlineKeyboardButton(text='✅ Приступить', callback_data=f'take_task:{task_number}')
        btn2 = InlineKeyboardButton(text='<', callback_data=f'last_task:{place-1}:{category}')
        btn3 = InlineKeyboardButton(text='>', callback_data=f'next_task:{place+1}:{category}')
        btn4 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn2, btn3).add(btn4)
        return keyboard
    

def user_my_category_kb(my_cat):
    keyboard = InlineKeyboardMarkup()
    if len(my_cat) != 0:
        for cat in my_cat:
            btn = InlineKeyboardButton(text=cat, callback_data=f'my_tasks:{cat}')
            keyboard.add(btn)
    else:
        btn = InlineKeyboardButton(text='Список пуст', callback_data='nothing')
        btn3 = InlineKeyboardButton(text='<<', callback_data=f'back_tasks')
        keyboard.add(btn).add(btn3)
    return keyboard

def user_my_tasks_select(cat):
    btn1 = InlineKeyboardButton(text='❎ нужно сдать', callback_data=f'my_active_tasks:{cat}')
    btn2 = InlineKeyboardButton(text='✅ оцененные', callback_data=f'my_done_tasks:{cat}')
    btn3 = InlineKeyboardButton(text='<<', callback_data=f'back_tasks')
    keyboard = InlineKeyboardMarkup().add(btn1, btn2).add(btn3)
    return keyboard


def my_task_active_kb(place, category, task_number):
    btn1 = InlineKeyboardButton(text='❎ Сдать', callback_data=f'hand_task:{task_number}')
    btn5 = InlineKeyboardButton(text='❌ Отказаться', callback_data=f'cancel_task:{task_number}')
    btn2 = InlineKeyboardButton(text='<', callback_data=f'active_last_my_task:{place-1}:{category}')
    btn3 = InlineKeyboardButton(text='>', callback_data=f'active_next_my_task:{place+1}:{category}')
    btn4 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn5).add(btn2, btn3).add(btn4)
    return keyboard

def new_task_accept_kb(task_number):
    btn1 = InlineKeyboardButton(text='❎ Сдать', callback_data=f'hand_task:{task_number}')
    btn2 = InlineKeyboardButton(text='❌ Отказаться', callback_data=f'cancel_task:{task_number}')
    btn3 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2).add(btn3)
    return keyboard

def cancel_task_kb():
    btn3 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
    keyboard = InlineKeyboardMarkup().add(btn3)
    return keyboard


def confiramtion_file_kb():
    btn1 = InlineKeyboardButton(text='пропустить', callback_data='skip_file_confirmation')
    btn2 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
    return keyboard

def confiramtion_text_kb():
    btn1 = InlineKeyboardButton(text='пропустить', callback_data='skip_text_confirmation')
    btn2 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
    keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
    return keyboard

def search_kb(task_number, in_process=False, checking=False, default=False):
    if in_process:
        btn1 = InlineKeyboardButton(text='❎ Сдать', callback_data=f'hand_task:{task_number}')
        btn2 = InlineKeyboardButton(text='❌ Отказаться', callback_data=f'cancel_task:{task_number}')
        btn3 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn2).add(btn3)
        return keyboard
    elif checking:
        btn1 = InlineKeyboardButton(text='📎 На проверке', callback_data='nothing')
        btn2 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
        return keyboard
    elif default:
        btn1 = InlineKeyboardButton(text='✅ Приступить', callback_data=f'take_task:{task_number}')
        btn2 = InlineKeyboardButton(text='<<', callback_data='back_tasks')
        keyboard = InlineKeyboardMarkup().add(btn1).add(btn2)
        return keyboard

def user_edit_text_kb():
    btn1 = InlineKeyboardButton(text='Понятно', callback_data='edit_text_back')
    keyboard = InlineKeyboardMarkup().add(btn1)
    return keyboard

