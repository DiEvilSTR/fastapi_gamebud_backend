from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class BudMatch(Timestamp, Base):
    """
    BudMatch model

    Fields:
    - **id**: Match id
    - **user_one_id**: First user id
    - **user_two_id**: Second user id
    """
    __tablename__ = "bud_matches"

    id = Column(Integer, primary_key=True, index=True)
    user_one_id = Column(String, ForeignKey("users.uuid"))
    user_two_id = Column(String, ForeignKey("users.uuid"))
