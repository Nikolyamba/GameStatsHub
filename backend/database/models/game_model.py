from sqlalchemy import Column, Integer, String, Float

from backend.database.session import Base

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    genre = Column(String)
    rating = Column(Float, nullable=True)
