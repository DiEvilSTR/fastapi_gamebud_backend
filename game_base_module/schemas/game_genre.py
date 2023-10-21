from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class GameGenreBase(BaseModel):
    """
    Base class for GameGenre

    Fields:
    - **name**: Game genre name
    - **description**: Game genre description
    """
    name: str
    description: Optional[str] = None


class GameGenreCreate(GameGenreBase):
    """
    Create class for GameGenre

    Fields:
    - **name**: Game genre name
    - **description**: Game genre description
    """
    pass


class GameGenreUpdate(GameGenreBase):
    """
    Update class for GameGenre

    Fields:
    - **name**: Game genre name
    - **description**: Game genre description
    """
    name: Optional[str] = None
    description: Optional[str] = None


class GameGenre(GameGenreBase):
    """
    Read class for GameGenre

    Fields:
    - **id**: Game genre id
    - **name**: Game genre name
    - **description**: Game genre description
    - **number_of_games**: Number of games associated with this genre
    - **created_at**: Game genre creation datetime
    - **updated_at**: Game genre update datetime
    """
    id: int
    name: str
    description: Optional[str] = None
    number_of_games: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GameGenreForList(BaseModel):
    """
    Read class for read list responses

    Fields:
    - **id**: Game genre id
    - **name**: Game genre name
    - **number_of_games**: Number of games associated with this genre
    """
    id: int
    name: str
    number_of_games: int

    class Config:
        from_attributes = True


class GameGenreForInGameList(BaseModel):
    """
    Read class for game info list responses

    Fields:
    - **id**: Game genre id
    - **name**: Game genre name
    """
    id: int
    name: str

    class Config:
        from_attributes = True
