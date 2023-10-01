from sqlalchemy import Boolean, Column, ForeignKey, String

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp


class BudLike(Timestamp, Base):
    """
    UserLike model

    Fields:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    - **is_like**: Another user was liked or disliked
    """
    __tablename__ = "user_likes"

    swiper_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
    swiped_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
    is_like = Column(Boolean, nullable=False)
