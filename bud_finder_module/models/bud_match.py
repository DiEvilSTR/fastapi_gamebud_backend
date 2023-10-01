from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class BudMatch(Timestamp, Base):
    """
    UserMatch model

    Fields:
    - **id**: Match id
    - **user_one_id**: First user id
    - **user_two_id**: Second user id
    
    Relationships:
    - **first_like**: First user like
    - **second_like**: Second user like
    """
    __tablename__ = "user_matches"

    id = Column(Integer, primary_key=True, index=True)
    user_one_id = Column(String, ForeignKey("users.uuid"))
    user_two_id = Column(String, ForeignKey("users.uuid"))
    
    # Relationships
    first_like = relationship("BudLike", foreign_keys=[user_one_id], uselist=False, delete_orphan=True)
    second_like = relationship("BudLike", foreign_keys=[user_one_id], uselist=False, delete_orphan=True)
