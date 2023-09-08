from pydantic import BaseModel


class GameGenreAssociationBase(BaseModel):
    game_id: int
    genre_id: int


class GameGenreAssociationCreate(GameGenreAssociationBase):
    pass


class GameGenreAssociationUpdate(GameGenreAssociationBase):
    pass


class GameGenreAssociation(GameGenreAssociationBase):
    game_id: int
    genre_id: int

    class Config:
        from_attributes = True
