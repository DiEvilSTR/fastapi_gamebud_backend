from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, List

from game_base_module.schemas.game import GameForUserProfileData
from core.constants import GenderEnum, CountryEnum


class UserBase(BaseModel):
    """
    Base class for User

    Fields:
    - **nickname**: User nickname
    """
    nickname: str


class UserCreate(UserBase):
    """
    Create class for User

    Fields:
    - **email**: User email
    - **birthday**: User birthday
    - **gender**: User gender
    - **password**: User password
    - **country**: User country
    """
    email: EmailStr
    birthday: datetime
    gender: GenderEnum
    password: str
    country: CountryEnum


class UserUpdate(UserBase):
    """
    Update class for User

    Fields:
    - **nickname**: User nickname
    - **birthday**: User birthday
    - **bio**: User bio
    - **games**: List of games associated with this user
    - **gender**: User gender
    - **country**: User country
    """
    nickname: Optional[str] = None
    birthday: Optional[datetime] = None
    bio: Optional[str] = None
    games: Optional[List[int]] = None
    gender: Optional[GenderEnum] = None
    country: Optional[CountryEnum] = None


class UserDeactivate(UserBase):
    """
    User deactivate class

    Fields:
    - **is_active**: User active status
    """
    is_active: bool = False


class User(UserBase):
    """
    Read class for User

    Fields:
    - **uuid**: User uuid
    - **nickname**: User nickname
    - **age**: User age
    - **gender**: User gender
    - **bio**: User bio
    - **games**: List of games associated with this user
    - **country**: User country
    """
    uuid: str
    nickname: str
    age: int
    gender: GenderEnum
    bio: Optional[str] = None
    games: Optional[List[GameForUserProfileData]] = []
    country: CountryEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserInDBForUpdate(UserBase):
    """
    User in database for update class

    Fields:
    - **birthday**: User birthday
    - **bio**: User bio
    - **games**: List of games associated with this user
    - **gender**: User gender
    - **country**: User country
    """
    birthday: datetime
    bio: Optional[str] = None
    games: Optional[List[GameForUserProfileData]] = []
    gender: GenderEnum
    country: CountryEnum

    class Config:
        from_attributes = True


class UserAsBud(UserBase):
    """
    Read class for User

    Fields:
    - **uuid**: User uuid
    - **nickname**: User nickname
    - **age**: User age
    - **gender**: User gender
    - **bio**: User bio
    - **games**: List of games associated with this user
    - **country**: User country
    """
    uuid: str
    nickname: str
    age: int
    bio: Optional[str] = None
    gender: GenderEnum
    games: Optional[List[GameForUserProfileData]] = []
    country: CountryEnum

    class Config:
        from_attributes = True
