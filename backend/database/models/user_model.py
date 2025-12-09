from sqlalchemy import Column, Integer, String

from backend.database.session import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(30), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(128))

