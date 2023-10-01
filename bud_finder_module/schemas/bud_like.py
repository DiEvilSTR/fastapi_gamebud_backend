from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BudLikeBase(BaseModel):
    """
    Base class for BudLike

    Fields:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    - **is_like**: Another user was liked or disliked
    """
    swiper_id: str
    swiped_id: str
    is_like: bool


class BudLikeCreate(BudLikeBase):
    '''
    Create class for BudLike

    Fields:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    - **is_like**: Another user was liked
    '''
    is_like: Optional[bool] = True


class BudDislikeCreate(BudLikeBase):
    '''
    Create class for BudDislike

    Fields:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    - **is_like**: Another user was disliked
    '''
    is_like: Optional[bool] = False


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
    created_at: datetime
    updated_at: datetime
