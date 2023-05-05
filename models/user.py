from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"

    user_id = Column(Integer, nullable=False, primary_key=True, unique=True)
    username = Column(String(16), nullable=False)
    hashed_password = Column(String, nullable=False)
    experience = Column(Integer, nullable=False)

    history = relationship("MatchHistory", back_populates="user", cascade="all, delete-orphan")