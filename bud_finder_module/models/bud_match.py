from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp

from chat_module.models.chat_message import ChatMessage


class BudMatch(Timestamp, Base):
    """
    BudMatch model

    Fields:
    - **id**: Match id

    Relationships:
    - **buds**: Users who have this match
    - **messages**: Messages in this match
    """
    __tablename__ = "bud_matches"

    id = Column(Integer, primary_key=True, index=True)

    # Define the relationship to the User model
    buds = relationship(
        "User", secondary="bud_match_associations", back_populates="matches")

    # Define the relationship to the Message model
    chat_messages = relationship(
        "ChatMessage", back_populates="match", cascade="all, delete-orphan")
