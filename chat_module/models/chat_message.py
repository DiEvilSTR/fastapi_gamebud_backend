from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class ChatMessage(Timestamp, Base):
    """
    Message model

    Fields:
    - **id**: Message id
    - **content**: Message content
    - **sender_id**: Sender id
    - **match_id**: Match id

    Relationships:
    - **match**: Match where the message was sent
    """
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    sender_id = Column(String, ForeignKey("users.uuid"))
    match_id = Column(Integer, ForeignKey("bud_matches.id"))

    # Define the relationship to the BudMatch model
    match = relationship("BudMatch", back_populates="chat_messages", uselist=False)
