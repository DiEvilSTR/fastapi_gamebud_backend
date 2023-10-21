from datetime import datetime
from pydantic import BaseModel


class BudLikeBase(BaseModel):
    """
    Base class for BudLike

    Fields:
    - **swiped_id**: Swiped id
    - **is_like**: Another user was liked or disliked
    """
    swiped_id: str
    is_like: bool


class BudLikeCreate(BudLikeBase):
    '''
    Create class for BudLike

    Fields:
    - **swiped_id**: Swiped id
    - **is_like**: Another user was liked
    '''
    is_like: bool


class BudLikeUpdate(BudLikeBase):
    pass


class BudLike(BudLikeBase):
    """
    Read class for BudLike

    Fields:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    - **is_like**: Another user was liked or disliked
    - **created_at**: BudLike creation datetime
    - **updated_at**: BudLike update datetime
    """
    swiper_id: str
    swiped_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
