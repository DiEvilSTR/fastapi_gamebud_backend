from datetime import datetime
import uuid as uuid_pkg

from sqlalchemy import Boolean, Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class User(Timestamp, Base):
    """
    User model

    Fields:
    - **uuid**: User uuid
    - **email**: User email
    - **hashed_password**: User hashed password
    - **nickname**: User nickname
    - **bio**: User bio
    - **is_active**: User is active
    - **is_superuser**: User is superuser

    Relationships:
    - **games**: User games
    """
    __tablename__ = "users"

    uuid: uuid_pkg.UUID = Column(
        String,
        primary_key=True,
        index=True,
        default=str(uuid_pkg.uuid4()),
        nullable=False,
        unique=True,
    )
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    nickname = Column(String(16), nullable=False)
    birthday = Column(DateTime, nullable=False)
    bio = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    @hybrid_property
    def count_age(self):
        return (datetime.now() - self.birthday).days // 365

    # Define the relationship to Game model
    games = relationship(
        "Game", secondary="user_game_association", back_populates="users")
