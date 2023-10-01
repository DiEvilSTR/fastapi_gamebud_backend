from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class BudLike(Timestamp, Base):
    """
    UserLike model

    Fields:
    - **id**: Like id
    - **swiper_id**: User who liked
    - **swiped_id**: User who was liked
    - **is_like**: True if user liked, False if disliked
    """
    __tablename__ = "user_likes"

    id = Column(Integer, primary_key=True, index=True)
    swiper_id = Column(String, ForeignKey("users.uuid"))
    swiped_id = Column(String, ForeignKey("users.uuid"))
    is_like = Column(Boolean, nullable=False)
