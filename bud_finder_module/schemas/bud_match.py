from datetime import datetime
from pydantic import BaseModel


class BudMatchBase(BaseModel):
    """
    Base class for BudMatch

    Fields:
    - **user_one_id**: User one id
    - **user_two_id**: User two id
    """
    user_one_id: str
    user_two_id: str


class BudMatchCreate(BudMatchBase):
    """
    Create class for BudMatch
    
    Fields:
    - **user_one_id**: User one id
    - **user_two_id**: User two id
    """
    pass


class BudMatchUpdate(BudMatchBase):
    """
    Update class for BudMatch
    
    Fields:
    - **user_one_id**: User one id
    - **user_two_id**: User two id
    """
    pass


class BudMatch(BudMatchBase):
    """
    Read class for BudMatch

    Fields:
    - **user_one_id**: User one id
    - **user_two_id**: User two id
    - **created_at**: BudMatch creation datetime
    - **updated_at**: BudMatch update datetime
    """
    created_at: datetime
    updated_at: datetime
