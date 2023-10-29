from datetime import datetime
from pydantic import BaseModel


class ChatMessageBase(BaseModel):
    """
    Base class for ChatMessage

    Fields:
    - **match_id**: Match id
    - **content**: Message content
    """
    match_id: int
    content: str


class ChatMessageCreate(ChatMessageBase):
    """
    Create class for ChatMessage

    Fields:
    - **match_id**: Match id
    - **content**: Message content
    """
    pass


class ChatMessage(ChatMessageBase):
    """
    Read class for ChatMessage

    Fields:
    - **id**: Message id
    - **match_id**: Match id
    - **sender_id**: Sender id
    - **content**: Message content
    - **created_at**: ChatMessage creation datetime
    - **updated_at**: ChatMessage update datetime
    """
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
