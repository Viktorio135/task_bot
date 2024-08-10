from sqlalchemy.orm import Session
from sqlalchemy import or_
from asgiref.sync import sync_to_async
import datetime
from .models import User, engine, Category, Task, TaskHistory, ArchiveTasks



@sync_to_async
def create_user(
    user_name,
    user_id,
    ):
    try:
        with Session(autoflush=False, bind=engine) as session:
            new_user = User(
                user_name=user_name,
                user_id=user_id,
            )
            session.add(new_user)
            session.commit()
            return 1
    except:
        return 0
    
@sync_to_async
def create_user_history(user_id):
    try:
        with Session(autoflush=False, bind=engine) as session:
            new_history = TaskHistory(
                user_id=user_id
            )
            session.add(new_history)
            session.commit()
            return 1
    except:
        return 0

@sync_to_async
def get_users_active_tasks(user_id, active_tasks):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
            if active_tasks:
                return obj.active_tasks
            else:
                return obj.history_tasks
    except:
        return 0


@sync_to_async
def block_user(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.is_block = True
        session.commit()




@sync_to_async 
def adding_new_activa_task(user_id, task_number):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
            obj.active_tasks += f'{task_number} '
            session.commit()
            return 1
    except:
        return 0

def get_list_of_blocks():
    with Session(autoflush=False, bind=engine) as session:
        block_users = set()
        obj = session.query(User).filter(User.is_block == True).all()
        if obj:
            for user in obj:
                block_users.add(int(user.user_id))
            return block_users
        else:
            return block_users



@sync_to_async
def adding_new_done_task(user_id, task_number):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
            obj.done_tasks += f'{task_number} '
            session.commit()
            return 1
    except:
        return 0
    
@sync_to_async 
def adding_new_history_task(user_id, task_number):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
            obj.history_tasks += f'{task_number} '
            session.commit()
            return 1
    except:
        return 0   

    
@sync_to_async
def delete_active_task(user_id, task_number):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
            obj.active_tasks = obj.active_tasks.replace(f'{task_number} ', '')
            session.commit()
    except:
        pass

@sync_to_async
def delete_history_task(user_id, number_task):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
            obj.history_tasks = obj.history_tasks.replace(f'{number_task} ', '')
            session.commit()
    except:
        pass


    


@sync_to_async
def adding_referal(user_id):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(User).filter(User.user_id == user_id).first()
            obj.ref_invitees += 1
            session.commit()
            return 1
    except:
        return 0
    
@sync_to_async
def adding_wallet(user_id, type_bank, card_number, bank_name, phone_number):
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(User).filter(User.user_id == user_id).first()
            obj.type_bank = type_bank
            obj.card_number = card_number
            obj.bank_name = bank_name
            obj.phone_number = phone_number
            session.commit()
            return 1
    

@sync_to_async
def get_user_data(user_id):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(User).filter(User.user_id == user_id).first()
            if not(obj):
                return 0
            data = {
                "user_name": obj.user_name,
                "user_id": obj.user_id,
                "ref_invitees": obj.ref_invitees,
                "balance": obj.balance,
                "type_bank": obj.type_bank,
                "card_number": obj.card_number,
                "bank_name": obj.bank_name,
                "phone_number": obj.phone_number,
                "notifications": obj.notifications,
                "youtube": obj.youtube,
                "in_process": obj.in_process,
                "done": obj.done,
                "cancelled": obj.cancelled,
                "rejected": obj.rejected,
                "times": obj.times
            }
            return data
    except:
        return 0

@sync_to_async
def get_user_data_by_username(username):
    try:
        with Session(autoflush=False, bind=engine) as session:
            obj = session.query(User).filter(User.user_name == username).first()
            if not(obj):
                return 0
            data = {
                "user_name": obj.user_name,
                "user_id": obj.user_id,
                "ref_invitees": obj.ref_invitees,
                "balance": obj.balance,
                "type_bank": obj.type_bank,
                "card_number": obj.card_number,
                "bank_name": obj.bank_name,
                "phone_number": obj.phone_number,
                "notifications": obj.notifications,
                "youtube": obj.youtube,
                "in_process": obj.in_process,
                "done": obj.done,
                "cancelled": obj.cancelled,
                "rejected": obj.rejected,
                "times": obj.times
            }
            return data
    except:
        return 0

@sync_to_async
def adding_user_in_process(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.in_process = obj.in_process + 1
        session.commit()

@sync_to_async
def adding_user_times(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.times = obj.times + 1
        session.commit()

@sync_to_async
def adding_user_done(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.done = obj.done + 1
        session.commit()

@sync_to_async
def adding_user_cancelled(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.cancelled = obj.cancelled + 1
        session.commit()

@sync_to_async
def adding_user_rejected(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.rejected = obj.rejected + 1
        session.commit()

@sync_to_async
def adding_user_warnings(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.warnings = obj.warnings + 1
        session.commit()

@sync_to_async
def subtract_user_in_process(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.in_process = obj.in_process - 1
        session.commit()

@sync_to_async
def subtract_user_cancelled(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.cancelled = obj.cancelled - 1
        session.commit()

@sync_to_async
def subtract_user_cancelled(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.rejected = obj.rejected - 1
        session.commit()

@sync_to_async
def adding_balance(user_id, reward):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.balance = obj.balance + int(reward)
        session.commit()

@sync_to_async
def subtract_balance(user_id, reward):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(User).filter(User.user_id == user_id).first()
        obj.balance = obj.balance - int(reward)
        session.commit()

@sync_to_async
def has_register(user_id):
    with Session(autoflush=False, bind=engine) as session:
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            return 1 if user else 0
        except: 
            pass


@sync_to_async
def change_notifications(user_id, params):
    with Session(autoflush=False, bind=engine) as session:
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            user.notifications = params
            session.commit()
            return 1
        except:
            pass


@sync_to_async
def change_youtube(user_id, link):
    with Session(autoflush=False, bind=engine) as session:
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            user.youtube = link
            session.commit()
            return 1
        except:
            return 0

@sync_to_async
def get_category(list=False):
        with Session(autoflush=False, bind=engine) as session:
            category = session.query(Category).all()
            if not list:
                return category
            else:
                sp = []
                if len(category) != 0:
                    for cat in category:
                        sp.append(cat.name)
                return sp
            
@sync_to_async
def adding_category(name):
    with Session(autoflush=False, bind=engine) as session:
        new_cat = Category(
            name=name
        )
        session.add(new_cat)
        session.commit()


@sync_to_async
def adding_task(
    category,
    full_text,
    small_text,
    price,
    timer,
    count_people,
    start_date,
    who_created,
):
    with Session(autoflush=False, bind=engine) as session:
        new_task = Task(
            category=category,
            full_text=full_text,
            small_text=small_text,
            price=price,
            timer=timer,
            count_people=count_people,
            start_date=start_date,
            who_created=who_created
        )
        session.add(new_task)
        session.commit()

@sync_to_async
def get_last_task():
    with Session(autoflush=False, bind=engine) as session:
        tasks = session.query(Task).all()
        if len(tasks) != 0:
            return tasks[-1].id
        return 0
    

@sync_to_async
def change_is_admin(user_id, is_admin):
    with Session(autoflush=False, bind=engine) as session:
        user = session.query(User).filter(User.user_id == user_id).first()
        user.is_admin = is_admin
        session.commit()

@sync_to_async
def get_users_list_for_task():
    with Session(autoflush=False, bind=engine) as session:
        sp = []
        users = session.query(User).all()
        for user in users:
            if (user.is_admin == False) and (user.notifications[1] == '1') and (user.is_block == False):
                sp.append(user.user_id)
        return sp
    

@sync_to_async
def get_task_datas(id):
    with Session(autoflush=False, bind=engine) as session:
        task = session.query(Task).filter(Task.id == id).first()
        if task is None:
            task = session.query(ArchiveTasks).filter(ArchiveTasks.number_task == id).first()
            if task is None:
                return 0
            data = {
                'id': task.number_task,
                'category': task.category,
                'full_text': task.full_text + '\n\nЗадание перенесено в архив',
                'small_text': task.small_text,
                'price': task.price,
                'timer': task.timer,
                'count_people': task.count_people,
                'start_date': task.start_date,
                'who_created': task.who_created,
            }
            return data
        data = {
            'id': task.id,
            'category': task.category,
            'full_text': task.full_text,
            'small_text': task.small_text,
            'price': task.price,
            'timer': task.timer,
            'count_people': task.count_people,
            'start_date': task.start_date,
            'who_created': task.who_created,
        }
        return data
    
@sync_to_async
def get_archive_task_datas(number_task):
    with Session(autoflush=False, bind=engine) as session:
        task = session.query(ArchiveTasks).filter(ArchiveTasks.number_task == number_task).first()
        if task is None:
            return 0
        data = {
            'number_task': task.number_task,
            'category': task.category,
            'full_text': task.full_text,
            'small_text': task.small_text,
            'price': task.price,
            'timer': task.timer,
            'count_people': task.count_people,
            'start_date': task.start_date,
            'end_date': task.end_date,
            'who_created': task.who_created,
            'rejected': task.rejected,
            'cancelled': task.cancelled,
            'times': task.times,
            'done': task.done
        }
        return data


@sync_to_async
def delete_task(id):
    with Session(autoflush=False, bind=engine) as session:
        session.query(Task).filter(Task.id == id).delete()
        session.commit()

        

@sync_to_async
def edit_task_text(id, text):
    with Session(autoflush=False, bind=engine) as session:
        task = session.query(Task).filter(Task.id == id).first()
        task.full_text = text
        session.commit()



async def get_done_task_users(number_task):
    with Session(autoflush=False, bind=engine) as session:
        sp = []
        users = session.query(TaskHistory).filter(
            or_(
                TaskHistory.done_tasks == number_task,  # Если `done_tasks` состоит только из этого числа
                TaskHistory.done_tasks.like(f'{number_task} %'),  # Если `done_tasks` начинается с этого числа
                TaskHistory.done_tasks.like(f'% {number_task} %'),  # Если `done_tasks` содержит это число в середине
                TaskHistory.done_tasks.like(f'% {number_task}')  # Если `done_tasks` заканчивается на это число
            )
        ).all()
        if users:
            for user in users:
                username = await get_user_data(user.user_id)
                sp.append((user.user_id, username["user_name"]))
            return sp
        else:
            return 0


@sync_to_async
def get_all_tasks():
    with Session(autoflush=False, bind=engine) as session:
        tasks = session.query(Task).all()
        return tasks
    
@sync_to_async
def get_all_archive_tasks():
    with Session(autoflush=False, bind=engine) as session:
        tasks = session.query(ArchiveTasks).all()
        return tasks
    
@sync_to_async
def get_all_archive_tasks_list():
    with Session(autoflush=False, bind=engine) as session:
        tasks = session.query(ArchiveTasks).all()
        if not tasks:
            return []
        sp = []
        for task in tasks:
            sp.append(task.number_task)
        return sp
        

@sync_to_async
def get_all_task_in_category(category):
    with Session(autoflush=False, bind=engine) as session:
        tasks = session.query(Task).filter(Task.category == category).all()
        return tasks
    
@sync_to_async
def get_count_task_in_category(category):
    with Session(autoflush=False, bind=engine) as session:
        count = session.query(Task).filter(Task.category == category).count()
        return count
    

@sync_to_async
def get_user_category(user_id):
    with Session(autoflush=False, bind=engine) as session:
        categories = []
        user_history = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
        active_tasks = user_history.active_tasks.split(' ')
        if len(active_tasks) != 0 and active_tasks != ['']:
            for num in active_tasks:
                if num != '':
                    task = session.query(Task).filter(Task.id == int(num)).first()
                    categories.append(task.category)
        history_tasks = user_history.history_tasks.split(' ')
        if len(history_tasks) != 0 and history_tasks != ['']:
            for num in history_tasks:
                if num != '':
                    task = session.query(Task).filter(Task.id == int(num)).first()
                    if not task:
                        task = session.query(ArchiveTasks).filter(ArchiveTasks.number_task == int(num)).first()
                    categories.append(task.category)
        # in_process = user_history..split(' ')
        # if len(in_process) != 0 and in_process != ['']:
        #     for num in in_process:
        #         if num != '':
        #             task = session.query(Task).filter(Task.id == int(num)).first()
        #             categories.append(task.category)

        if ' ' in categories:
            categories.remove(' ')
        if '' in categories:
            categories.remove('')
        categories = list(set(categories))
        if categories == ['']:
            categories = []
        return categories


@sync_to_async
def get_users_task_active_by_category(user_id, category, task_progress):
    with Session(autoflush=False, bind=engine) as session:
        tasks_in_process = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
        tasks_in_process = tasks_in_process.active_tasks.split(' ')
        tasks = []
        for task in tasks_in_process:
            if task != '':
                obj = session.query(Task).filter(Task.id == int(task)).first()
                if obj.category == category:
                    tasks.append(obj.id)
        for task in list(tasks):
            if int(user_id) in task_progress[int(task)]['users']['checking']:
                tasks.remove(task)
        return tasks
    
@sync_to_async
def get_users_task_history_by_category(user_id, category):
    with Session(autoflush=False, bind=engine) as session:
        tasks_in_process = session.query(TaskHistory).filter(TaskHistory.user_id == user_id).first()
        tasks_in_process = tasks_in_process.history_tasks.split(' ')
        tasks = []
        for task in tasks_in_process:
            if task != '':
                obj = session.query(Task).filter(Task.id == int(task)).first()
                if not obj:
                    obj = session.query(ArchiveTasks).filter(ArchiveTasks.number_task == int(task)).first()
                    if obj.category == category:
                        tasks.append(obj.number_task)
                else:
                    tasks.append(obj.id)
        return tasks

    
@sync_to_async
def is_time_remaining(start_time, duration_minutes):
    if duration_minutes != '00':
        now = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=float(duration_minutes))
        if now < end_time:
            # Вычисление оставшегося времени в минутах
            remaining_time = (end_time - now).total_seconds() / 60
            return remaining_time
        else:
            return 0
    else:
        return 'Бессрочно'
    


@sync_to_async
def adding_archive_task(
    number_task,
    category,
    full_text,
    small_text,
    price,
    timer,
    count_people,
    start_date,
    end_date,
    who_created,
    rejected,
    cancelled,
    times,
    done
):
    with Session(autoflush=False, bind=engine) as session:
        new_task = ArchiveTasks(
            number_task=number_task,
            category=category,
            full_text=full_text,
            small_text=small_text,
            price=price,
            timer=timer,
            count_people=count_people,
            start_date=start_date,
            end_date=end_date,
            who_created=who_created,
            rejected=rejected,
            cancelled=cancelled,
            times=times,
            done=done
        )
        session.add(new_task)
        session.commit()

@sync_to_async
def get_all_active_tasks(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(TaskHistory).filter(TaskHistory.user_id == str(user_id)).first()
        if obj:
            return obj.active_tasks
        else:
            return 0
        
@sync_to_async
def get_all_history_tasks(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(TaskHistory).filter(TaskHistory.user_id == str(user_id)).first()
        if obj:
            return obj.history_tasks
        else:
            return 0
    
@sync_to_async
def get_all_done_tasks(user_id):
    with Session(autoflush=False, bind=engine) as session:
        obj = session.query(TaskHistory).filter(TaskHistory.user_id == str(user_id)).first()
        if obj:
            return obj.done_tasks
        else:
            return 0