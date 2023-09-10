from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class GameGenre(Timestamp, Base):
    """
    Game genre model

    Fields:
    - **id**: Game genre id
    - **name**: Game genre name
    - **description**: Game genre description
    """
    __tablename__ = "game_genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String(500), nullable=True)

    @hybrid_property
    def game_count(self):
        # Calculate the number of games associated with this genre
        return len(self.games)

    # Define the relationship to Game model
    games = relationship(
        "Game", secondary="game_genre_association", back_populates="genres")
