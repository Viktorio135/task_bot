import os
from dotenv import load_dotenv
from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Boolean, 
    Text, 
    ForeignKey,
    DateTime,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base


# Загрузка переменных окружения
load_dotenv()

user_bd = os.getenv('USER_BD')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')

# Базовый класс для декларативного стиля
Base = declarative_base()

# Создание движка для подключения к базе данных
engine = create_engine(f"mysql+mysqlconnector://{user_bd}:{password}@{host}/{database}")

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(100))
    user_id = Column(String(100))
    who_invite = Column(String(100), default='')
    ref_invitees = Column(Integer, default=0)
    balance = Column(Integer, default=0)
    type_bank = Column(String(100), default='')
    card_number = Column(String(100), default='')
    bank_name = Column(String(100), default='')
    phone_number = Column(String(100), default='')
    notifications = Column(String(3), default='111')
    youtube = Column(String(200), default='')
    is_admin = Column(Boolean, default=False)
    is_block = Column(Boolean, default=False)
    in_process = Column(Integer, default=0)
    done = Column(Integer, default=0)
    cancelled = Column(Integer, default=0)
    rejected = Column(Integer, default=0)
    times = Column(Integer, default=0)
    warnings = Column(Integer, default=0)


class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Task(Base):
    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True)
    category = Column(String(100))
    full_text = Column(Text(5000))
    small_text = Column(String(1000))
    price = Column(String(10))
    timer = Column(String(10))
    count_people = Column(String(10))
    start_date = Column(DateTime)
    who_created = Column(String(100))

class TaskHistory(Base):
    __tablename__ = 'task_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(100))
    active_tasks = Column(Text(5000), default='')
    history_tasks = Column(Text(10000), default='')
    done_tasks = Column(Text(10000), default='')

class ArchiveTasks(Base):
    __tablename__ = 'ArchiveTasks'
    id = Column(Integer, primary_key=True)
    number_task = Column(Integer)
    category = Column(String(100))
    full_text = Column(Text(5000))
    small_text = Column(String(1000))
    price = Column(String(10))
    timer = Column(String(10))
    count_people = Column(String(10))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    who_created = Column(String(100))
    rejected = Column(Integer)
    cancelled = Column(Integer)
    times = Column(Integer)
    done = Column(Integer)

class Statistic(Base):
    __tablename__ = 'statistic'
    id = Column(Integer, primary_key=True)
    paid = Column(Integer, default=0)
    count_tasks = Column(Integer, default=0)
    delete_tasks = Column(Integer, default=0)
    accepted = Column(Integer, default=0)
    rejected = Column(Integer, default=0)

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100))
    user_name = Column(String(100))
    amount = Column(Integer)
    date = Column(DateTime)




def start_db():
    Base.metadata.create_all(bind=engine, checkfirst=True)


