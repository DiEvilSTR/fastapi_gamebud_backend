import uuid as uuid_pkg

from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

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
    bio = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    # games = relationship("Game", back_populates="task_owner", cascade="all, delete-orphan")
