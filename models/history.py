from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp


class MatchHistory(Timestamp, Base):
    __tablename__ = "game_history"

    match_id = Column(Integer, primary_key=True, index=True)
    opponent = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    winner = Column(Integer, ForeignKey("user.user_id"), nullable=False)

    user = relationship("User", back_populates="history", uselist=False)