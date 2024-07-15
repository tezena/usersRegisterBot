# database.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_registered = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

def add_user(telegram_id, username, first_name, last_name):
    user = User(telegram_id=telegram_id, username=username, first_name=first_name, last_name=last_name)
    session.add(user)
    session.commit()

def user_exists(telegram_id):
    return session.query(User).filter_by(telegram_id=telegram_id).first() is not None
