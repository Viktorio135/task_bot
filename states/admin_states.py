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

class AdminSearchArchiveTask(StatesGroup):
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

class AdminSearchUser(StatesGroup):
    user_id = State()

class AdminAddingWarning(StatesGroup):
    user_id = State()
    text = State()

class AdminAddingBalance(StatesGroup):
    user_id = State()
    balance = State()

class AdminSubtractBalance(StatesGroup):
    user_id = State()
    balance = State()

class AdminGiveTask(StatesGroup):
    user_id = State()
    number_task = State()

class AdminSearchUserTask(StatesGroup):
    user_id = State()
    number_task = State()
    