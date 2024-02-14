from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from user_profile_module.schemas.user import UserAsBudForMatchList


class BudMatchBase(BaseModel):
    """
    Base class for BudMatch
    """
    pass


class BudMatchCreate(BudMatchBase):
    """
    Create class for BudMatch
    """
    pass


class BudMatch(BudMatchBase):
    """
    Read class for BudMatch

    Fields:
    - **id**: Match id
    - **buds**: Users who have this match
    - **messages**: Messages in this match (not implemented)
    """
    id: int
    buds: List[UserAsBudForMatchList]
    # messages: List[Message] = []

    class Config:
        from_attributes = True


class BudMatchForMatchList(BudMatchBase):
    """
    Read class for BudMatch for match list

    Fields:
    - **id**: Match id
    - **bud**: Opponent user id
    """
    id: int
    bud: UserAsBudForMatchList

    class Config:
        from_attributes = True
