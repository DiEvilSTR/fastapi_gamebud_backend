from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, List

from game_base_module.schemas.game import GameForUserProfileData
from user_profile_module.constants import GenderEnum


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
    - **password**: User password
    """
    email: EmailStr
    birthday: datetime
    gender: GenderEnum
    password: str


class UserUpdate(UserBase):
    """
    Update class for User

    Fields:
    - **nickname**: User nickname
    - **birthday**: User birthday
    - **bio**: User bio
    - **games**: List of games associated with this user
    """
    nickname: Optional[str] = None
    birthday: Optional[datetime] = None
    bio: Optional[str] = None
    games: Optional[List[int]] = None


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
    - **bio**: User bio
    - **games**: List of games associated with this user
    """
    uuid: str
    nickname: str
    age: int
    gender: GenderEnum
    bio: Optional[str] = None
    games: Optional[List[GameForUserProfileData]] = []
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
    """
    birthday: datetime
    bio: Optional[str] = None
    games: Optional[List[GameForUserProfileData]] = []

    class Config:
        from_attributes = True
