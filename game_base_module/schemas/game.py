from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from .game_genre import GameGenreForList


class GameBase(BaseModel):
    name: str
    description: Optional[str] = None
    genres: List[int]  # List of genre IDs


class GameCreate(GameBase):
    pass


class GameUpdate(GameBase):
    pass


class Game(GameBase):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    genres: List[GameGenreForList] = []

    class Config:
        from_attributes = True
