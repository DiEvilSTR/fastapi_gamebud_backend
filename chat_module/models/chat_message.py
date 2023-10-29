from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class ChatMessage(Timestamp, Base):
    """
    Message model

    Fields:
    - **id**: Message id
    - **match_id**: Match id
    - **sender_id**: Sender id
    - **content**: Message content
    """
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("bud_matches.id"))
    sender_id = Column(String, ForeignKey("users.uuid"))
    content = Column(String, nullable=False)

    # Define the relationship to the BudMatch model
    match = relationship("BudMatch", back_populates="chat_messages", uselist=False)
