import uuid as uuid_pkg

from sqlalchemy import Boolean, Column, Integer, Field, ForeignKey, String
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"

    uuid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True, index=True, nullable=False)
    username = Column(String(16), nullable=False)
    hashed_password = Column(String, nullable=False)
    bio = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    # games = relationship("Game", back_populates="task_owner", cascade="all, delete-orphan")