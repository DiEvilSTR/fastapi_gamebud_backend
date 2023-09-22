from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class Game(Timestamp, Base):
    """
    Game model

    Fields:
    - **id**: Game id
    - **name**: Game name
    - **description**: Game description

    Relationships:
    - **genres**: Game genres
    - **users**: Users who have this game
    """
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String(500), nullable=True)

    # Define the relationship to the GameGenre model
    genres = relationship(
        "GameGenre", secondary="game_genre_association", back_populates="games")
    users = relationship(
        "User", secondary="user_game_association", back_populates="games")
