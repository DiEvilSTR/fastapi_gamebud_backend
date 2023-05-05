from sqlalchemy import Column, ForeignKey, Integer, String

from db.db_setup import Base
from .mixins import Timestamp


class Match(Timestamp, Base):
    __tablename__ = "game_history"

    id = Column(Integer, primary_key=True, index=True)
    player1 = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    player1_ships = Column(String, nullable=False)
    player1_shots = Column(String, nullable=False)
    player2 = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    player2_ships = Column(String, nullable=False)
    player2_shots = Column(String, nullable=False)
    player_turn = Column(Integer, ForeignKey("user.user_id"), nullable=False)
