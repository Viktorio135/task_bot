from aiogram.dispatcher.filters.state import State, StatesGroup



class AdminNewCategory(StatesGroup):
    category = State()
    full_text = State()
    small_text = State()
    price = State()
    timer = State()
    count_people = State()
    confirmation = State()

class AdminSearchTask(StatesGroup):
    number_task = State()

class AdminEditText(StatesGroup):
    number_task = State()
    text = State()
    confirmation = State()

class AdminRejectTask(StatesGroup):
    place = State()
    user_id = State()
    number_task = State()
    couse = State()