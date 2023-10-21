from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from core.constants import CountryEnum, GenderEnum


class BudFilterBase(BaseModel):
    """
    Base class for BudBaseFilter

    Fields:
    - **min_age_preference**: Minimum preferred age
    - **max_age_preference**: Maximum preferred age
    - **country_preference**: Preferred country
    - **gender_preference**: Gender preference (list of strings)
    """
    min_age_preference: int
    max_age_preference: int
    country_preference: CountryEnum
    gender_preference: List[GenderEnum]


class BudFilterCreate(BudFilterBase):
    """
    Create class for BudBaseFilter

    Fields:
    - **min_age_preference**: Minimum preferred age
    - **max_age_preference**: Maximum preferred age
    - **country_preference**: Preferred country
    - **gender_preference**: Gender preference (list of strings)
    """
    pass


class BudFilterUpdate(BudFilterBase):
    """
    Update class for BudBaseFilter

    Fields:
    - **min_age_preference**: Minimum preferred age
    - **max_age_preference**: Maximum preferred age
    - **country_preference**: Preferred country
    - **gender_preference**: Gender preference (list of strings)
    """
    min_age_preference: Optional[int] = None
    max_age_preference: Optional[int] = None
    country_preference: Optional[CountryEnum] = None
    gender_preference: Optional[List[GenderEnum]] = None


class BudFilter(BudFilterBase):
    """
    Read class for BudFilter

    Fields:
    - **user_id**: User uuid
    - **min_age_preference**: Minimum preferred age
    - **max_age_preference**: Maximum preferred age
    - **country_preference**: Preferred country

    """
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Not using this class
class BudGenderFilterBase(BaseModel):
    """
    Base class for BudGenderFilter

    Fields:
    - **gender_preference**: User's gender preference
    """
    gender_preference: GenderEnum


# Not using this class
class BudGenderFilter(BudGenderFilterBase):
    """
    Read class for BudGenderFilter

    Fields:
    - **user_id**: User uuid
    - **gender_preference**: User's gender preference
    """
    user_id: str
    gender_preference: GenderEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
