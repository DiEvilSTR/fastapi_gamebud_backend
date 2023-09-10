from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme

from game_base_module.crud import game_crud, game_genre_crud, association_crud
from game_base_module.schemas.game import Game, GameCreate, GameUpdate
from game_base_module.schemas.game_genre import GameGenre, GameGenreCreate, GameGenreUpdate, GameGenreForList
from game_base_module.schemas.association import GameGenreAssociation

router = APIRouter()

# Game genre endpoints

@router.post("/game_genre", response_model=GameGenre, status_code=status.HTTP_201_CREATED)
def add_new_game_genre(game_genre: GameGenreCreate, db: Session = Depends(db_setup.get_db)):
    """
    Add a new game genre to the database
    
    Parameters:
    - **game_genre**: Game genre to be added
    """
    game_genre_in_db = game_genre_crud.get_game_genre_by_name(
        db=db, name=game_genre.name)
    if game_genre_in_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Game genre with this name is already registered."
        )
    # Add game genre to the database
    db_game_genre = game_genre_crud.add_game_genre(
        db=db, game_genre=game_genre)
    return db_game_genre


@router.get("/game_genre", response_model=List[GameGenreForList])
def get_game_genre_list(skip: int = 0, limit: int = 100, db: Session = Depends(db_setup.get_db)):
    """
    Get game genre list
    
    Parameters:
    - **skip**: Skip the first N game genres
    - **limit**: Limit the number of game genres returned
    """
    db_game_genre_list = game_genre_crud.get_game_genre_list(
        db=db, skip=skip, limit=limit)
    return db_game_genre_list


@router.get("/game_genre/{id}", response_model=GameGenre)
def get_game_genre_by_id(id: int, db: Session = Depends(db_setup.get_db)):
    """
    Get game genre by id
    
    Parameters:
    - **id**: Game genre id
    """
    db_game_genre = game_genre_crud.get_game_genre_by_id(db=db, id=id)
    if db_game_genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game genre with this id does not exists."
        )
    return db_game_genre


@router.patch("/game_genre/{id}", response_model=GameGenre)
def update_game_genre_by_id(id: int, game_genre: GameGenreUpdate, db: Session = Depends(db_setup.get_db)):
    """
    Update game genre by id
    
    Parameters:
    - **id**: Game genre id
    - **game_genre**: Updated game genre data
    """
    db_game_genre = game_genre_crud.get_game_genre_by_id(db=db, id=id)
    if db_game_genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game genre with this id does not exists."
        )
    db_game_genre = game_genre_crud.update_game_genre(
        db=db, game_genre=game_genre, id=id)
    return db_game_genre


@router.delete("/game_genre/{id}")
def delete_game_genre_by_id(id: int, db: Session = Depends(db_setup.get_db)):
    """
    Delete game genre by id
    
    Parameters:
    - **id**: Game genre id
    """
    db_game_genre = game_genre_crud.get_game_genre_by_id(db=db, id=id)
    if db_game_genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game genre already deleted."
        )
    game_genre_crud.delete_game_genre(db=db, id=id)
    return {"detail": f"Game genre with id {id} deleted successfully."}


# Games endpoints

@router.post("/game", response_model=Game, status_code=status.HTTP_201_CREATED)
def add_new_game(game: GameCreate, db: Session = Depends(db_setup.get_db)):
    """
    Add a new game to the database
    
    Parameters:
    - **game**: Game to be added
    """
    game_in_db = game_crud.get_game_by_name(db=db, name=game.name)
    if game_in_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Game with this name is already registered."
        )
    # Add game to the database and get the game id
    db_game_id = game_crud.add_game(db=db, game=game)
    # Add game genre associations to the database
    association_crud.add_association(
        db=db, game_id=db_game_id, association_list=game.genre_list)
    # Get the game from the database
    db_game = game_crud.get_game_by_id(db=db, id=db_game_id)
    return db_game


@router.get("/game", response_model=List[Game])
def get_game_list(skip: int = 0, limit: int = 100, search: str = None, db: Session = Depends(db_setup.get_db)):
    """
    Get game list
    
    Parameters:
    - **skip**: Skip the first N games
    - **limit**: Limit the number of games returned
    - **search**: Search games by name
    """
    db_game_list = game_crud.get_game_list_with_search_parameters(
        db=db, skip=skip, limit=limit, search=search)
    return db_game_list


# Get game by id
@router.get("/game/{id}", response_model=Game)
def get_game_by_id(id: int, db: Session = Depends(db_setup.get_db)):
    """
    Get game by id
    
    Parameters:
    - **id**: Game id
    """
    db_game = game_crud.get_game_by_id(db=db, id=id)
    if db_game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game with this id does not exists."
        )
    return db_game


@router.patch("/game/{id}", response_model=Game)
def update_game_by_id(id: int, game: GameUpdate, db: Session = Depends(db_setup.get_db)):
    """
    Update game by id
    
    Parameters:
    - **id**: Game id
    - **game**: Updated game data
    """
    db_game = game_crud.get_game_by_id(db=db, id=id)
    if db_game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game with this id does not exists."
        )
    db_game = game_crud.update_game(db=db, game=game, id=id)
    return db_game


@router.delete("/game/{id}")
def delete_game_by_id(id: int, db: Session = Depends(db_setup.get_db)):
    """
    Delete game by id
    
    Parameters:
    - **id**: Game id
    """
    db_game = game_crud.get_game_by_id(db=db, id=id)
    if db_game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game already deleted."
        )
    game_crud.delete_game(db=db, id=id)
    return {"detail": f"Game with id {id} deleted successfully."}
