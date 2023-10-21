from datetime import datetime
import uuid as uuid_pkg

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp

from core.constants import GenderEnum, CountryEnum


class User(Timestamp, Base):
    """
    User model

    Fields:
    - **uuid**: User uuid
    - **email**: User email
    - **hashed_password**: User hashed password
    - **nickname**: User nickname
    - **birthday**: User birthday
    - **gender**: User gender
    - **bio**: User bio
    - **is_active**: User is active
    - **is_superuser**: User is superuser

    Properties:
    - **age**: User age

    Relationships:
    - **games**: User games
    - **base_filters**: User base filters (one-to-one)
    - **gender_filter**: User gender filters (one-to-many)
    """
    __tablename__ = "users"

    uuid: uuid_pkg.UUID = Column(
        String,
        primary_key=True,
        index=True,
        nullable=False,
        unique=True
    )
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    nickname = Column(String(16), nullable=False)
    birthday = Column(DateTime, nullable=False)
    gender = Column(ENUM(GenderEnum), nullable=False)
    bio = Column(String(500), nullable=True)
    country = Column(ENUM(CountryEnum), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    # Define the relationship to Game model
    games = relationship(
        "Game", secondary="user_game_association", back_populates="users")

    # Define the relationship to BudBaseFilter model
    filters = relationship(
        "BudBaseFilter", back_populates="owner", uselist=False, cascade="all, delete-orphan")
