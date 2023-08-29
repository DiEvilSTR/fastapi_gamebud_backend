from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    nickname: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    bio: Optional[str] = None


class UserDeactivate(UserBase):
    is_active: bool = False


class User(UserBase):
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
