from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class GameGenre(Timestamp, Base):
    __tablename__ = "game_genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String(500), nullable=True)

    # Define the relationship to Game model
    games = relationship(
        "Game", secondary="game_genre_association", cascade="all, delete")
