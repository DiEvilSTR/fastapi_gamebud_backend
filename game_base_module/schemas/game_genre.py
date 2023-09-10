from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class GameGenreBase(BaseModel):
    name: str
    description: Optional[str] = None


class GameGenreCreate(GameGenreBase):
    pass


class GameGenreUpdate(GameGenreBase):
    name: Optional[str] = None
    description: Optional[str] = None


class GameGenre(GameGenreBase):
    id: int
    name: str
    description: Optional[str] = None
    number_of_games: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GameGenreForList(BaseModel):
    id: int
    name: str
    number_of_games: int

    class Config:
        from_attributes = True


class GameGenreForInGameList(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True