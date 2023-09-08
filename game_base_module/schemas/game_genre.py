from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class GameGenreBase(BaseModel):
    name: str
    description: Optional[str] = None


class GameGenreCreate(GameGenreBase):
    pass


class GameGenreUpdate(GameGenreBase):
    pass


class GameGenre(GameGenreBase):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GameGenreForList(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
