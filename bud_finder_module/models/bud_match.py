from sqlalchemy import Column, ForeignKey, String

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class BudMatch(Timestamp, Base):
    """
    UserMatch model

    Fields:
    - **user_one_id**: User one id
    - **user_two_id**: User two id
    """
    __tablename__ = "user_matches"

    user_one_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
    user_two_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
