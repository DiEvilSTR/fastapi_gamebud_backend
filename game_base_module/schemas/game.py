from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from .game_genre import GameGenreForInGameList


class GameBase(BaseModel):
    """
    Base class for Game

    Fields:
    - **name**: Game name
    - **description**: Game description
    """
    name: str
    description: Optional[str] = None


class GameCreate(GameBase):
    """
    Create class for Game

    Fields:
    - **name**: Game name
    """
    genre_list: List[int]  # List of genre IDs


class GameUpdate(GameBase):
    """
    Update class for Game

    Fields:
    - **name**: Game name
    - **description**: Game description
    - **genre_list**: List of genre IDs
    """
    name: Optional[str] = None
    description: Optional[str] = None
    genre_list: Optional[List[int]] = None  # List of genre IDs


class Game(GameBase):
    """
    Read class for Game

    Fields:
    - **id**: Game id
    - **name**: Game name
    - **description**: Game description
    - **created_at**: Game creation datetime
    - **updated_at**: Game update datetime
    - **genres**: List of genres associated with this game
    """
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    genres: List[GameGenreForInGameList] = []

    class Config:
        from_attributes = True
