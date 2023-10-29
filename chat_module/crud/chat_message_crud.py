from sqlalchemy.orm import Session

from chat_module.models.chat_message import ChatMessage
from chat_module.schemas.chat_message import ChatMessageCreate


def save_message(db: Session, message: ChatMessageCreate, sender_id: str):
    """
    Save a message in the database

    Parameters:
    - **message**: Message to save in the database
    """
    db_message = ChatMessage(**message.model_dump(), sender_id=sender_id)
    db.add(db_message)
    db.commit()


def get_messages_by_match_id(db: Session, match_id: int, offset: int = 0, limit: int = 20):
    """
    Get messages from a match by match id

    Parameters:
    - **match_id**: Match id to get messages
    - **offset**: Offset of messages to get from the database (default: 0)
    - **limit**: Limit of messages to get from the database (default: 20)
    """
    return db.query(ChatMessage).filter(
        ChatMessage.match_id == match_id
    ).offset(offset).limit(limit).all()


# TODO: This function is not used, for admin purposes only
def get_messages_by_match_id_and_sender_id(db: Session, match_id: int, sender_id: str, offset: int = 0, limit: int = 20):
    """
    Get messages from a match by match id and sender id

    Parameters:
    - **match_id**: Match id to get messages
    - **sender_id**: Sender id to get messages
    - **offset**: Offset of messages to get from the database (default: 0)
    - **limit**: Limit of messages to get from the database (default: 20)
    """
    return db.query(ChatMessage).filter(
        ChatMessage.match_id == match_id,
        ChatMessage.sender_id == sender_id
    ).offset(offset).limit(limit).all()


def delete_all_messages_by_match_id(db: Session, match_id: int):
    """
    Delete all messages from a match by match id

    Parameters:
    - **match_id**: Match id to delete messages
    """
    db.query(ChatMessage).filter(
        ChatMessage.match_id == match_id
    ).delete(synchronize_session=False)
    db.commit()