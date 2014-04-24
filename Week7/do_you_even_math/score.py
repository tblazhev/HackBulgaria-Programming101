from base import Base
from sqlalchemy import Column, Integer, String


class Score(Base):
    __tablename__ = "highscores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
