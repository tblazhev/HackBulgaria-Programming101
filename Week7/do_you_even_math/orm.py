from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from base import Base

from score import Score

engine = create_engine("sqlite:///math.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
