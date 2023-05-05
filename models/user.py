from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"

    username = Column(String(16), nullable=False, primary_key=True, unique=True)
    hashed_password = Column(String, nullable=False)
