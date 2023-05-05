from datetime import datetime
from pydantic import BaseModel
from .history import MatchHistory


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    username: str
    experience: int
    created_at: datetime
    updated_at: datetime
    history: list[MatchHistory] = []

    class Config:
        orm_mode = True
