from pydantic import BaseModel


class GameGenreAssociationBase(BaseModel):
    """
    Base class for GameGenreAssociation

    Fields:
    - **game_id**: Game id
    - **genre_id**: Genre id
    """
    game_id: int
    genre_id: int


class GameGenreAssociationCreate(GameGenreAssociationBase):
    """
    Create class for GameGenreAssociation
    """
    pass


class GameGenreAssociationUpdate(GameGenreAssociationBase):
    """
    Update class for GameGenreAssociation
    """
    pass


class GameGenreAssociation(GameGenreAssociationBase):
    """
    Read class for GameGenreAssociation

    Fields:
    - **game_id**: Game id
    - **genre_id**: Genre id
    """
    game_id: int
    genre_id: int

    class Config:
        from_attributes = True
