from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class Message(Timestamp, Base):
    """
    Message model

    Fields:
    - **id**: Message id
    - **content**: Message content
    - **user_id**: User id
    - **chat_id**: Chat id

    Relationships:
    - **user**: User who sent the message
    - **chat**: Chat where the message was sent
    """
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))

    # Define the relationship to the User model
    user = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")
