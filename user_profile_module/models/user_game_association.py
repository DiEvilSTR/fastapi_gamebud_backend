from sqlalchemy import Column, Integer, ForeignKey, String
from core.db.db_setup import Base


class UserGameAssociation(Base):
    """
    User game association model

    Fields:
    - **user_id**: User id
    - **game_id**: Game id
    """
    __tablename__ = "user_game_association"

    user_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
