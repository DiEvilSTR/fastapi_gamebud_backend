from sqlalchemy import Column, Integer, ForeignKey
from core.db.db_setup import Base


class GameGenreAssociation(Base):
    __tablename__ = "game_genre_association"

    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("game_genres.id"), primary_key=True)
