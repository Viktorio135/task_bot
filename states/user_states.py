from aiogram.dispatcher.filters.state import State, StatesGroup



class StartWallet(StatesGroup):
    type_bank = State()
    card_number = State()
    bank_name = State()
    phone_number = State()


class AddingYoutube(StatesGroup):
    link = State()


class Confirmation(StatesGroup):
    task_number = State()
    file = State()
    text = State()

class SearchTask(StatesGroup):
    number_task = State()