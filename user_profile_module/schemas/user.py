from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


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
    - **password**: User password
    """
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """
    Update class for User

    Fields:
    - **bio**: User bio
    """
    bio: Optional[str] = None


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
    - **id**: User id
    - **uuid**: User uuid
    - **email**: User email
    - **nickname**: User nickname
    - **bio**: User bio
    - **is_active**: User active status
    - **is_superuser**: User superuser status
    - **created_at**: User creation datetime
    - **updated_at**: User update datetime
    """
    uuid: str
    email: EmailStr
    nickname: str
    bio: Optional[str] = None
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
