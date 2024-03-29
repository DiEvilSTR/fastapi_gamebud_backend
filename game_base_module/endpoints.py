from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme

from game_base_module.crud import game_crud, game_genre_association_crud, game_genre_crud
from game_base_module.schemas.game import Game, GameCreate, GameUpdate
from game_base_module.schemas.game_genre import GameGenre, GameGenreCreate, GameGenreUpdate, GameGenreForList
from game_base_module.schemas.game_genre_association import GameGenreAssociation

router = APIRouter()

# Game genre endpoints


@router.post("/game_genre", response_model=GameGenre, status_code=status.HTTP_201_CREATED, dependencies=[Depends(jwt_scheme)])
def add_new_game_genre(game_genre: GameGenreCreate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
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


@router.get("/game_genre", response_model=List[GameGenreForList], dependencies=[Depends(jwt_scheme)])
def get_game_genre_list(offset: int = 0, limit: int = 100, db: Session = Depends(db_setup.get_db)):
    """
    Get game genre list

    Parameters:
    - **offset**: Skip the first N game genres
    - **limit**: Limit the number of game genres returned
    """
    db_game_genre_list = game_genre_crud.get_game_genre_list(
        db=db, offset=offset, limit=limit)
    return db_game_genre_list


@router.get("/game_genre/{id}", response_model=GameGenre, dependencies=[Depends(jwt_scheme)])
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


@router.patch("/game_genre/{id}", response_model=GameGenre, dependencies=[Depends(jwt_scheme)])
def update_game_genre_by_id(id: int, game_genre: GameGenreUpdate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
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


@router.delete("/game_genre/{id}", dependencies=[Depends(jwt_scheme)])
def delete_game_genre_by_id(id: int, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
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

    # Delete game genre
    game_genre_crud.delete_game_genre(db=db, id=id)

    # Delete game genre associations
    game_genre_association_crud.delete_game_genre_association(
        db=db, genre_id=id)
    return {"detail": f"Game genre with id {id} deleted successfully."}


# Games endpoints


@router.post("/game", response_model=Game, status_code=status.HTTP_201_CREATED, dependencies=[Depends(jwt_scheme)])
def add_new_game(game: GameCreate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
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
    game_genre_association_crud.add_association(
        db=db, game_id=db_game_id, association_list=game.genre_list)
    # Get the game from the database
    db_game = game_crud.get_game_by_id(db=db, id=db_game_id)
    return db_game


@router.get("/game", response_model=List[Game], dependencies=[Depends(jwt_scheme)])
def get_game_list(offset: int = 0, limit: int = 100, search: str = None, db: Session = Depends(db_setup.get_db)):
    """
    Get game list

    Parameters:
    - **offset**: Skip the first N games
    - **limit**: Limit the number of games returned
    - **search**: Search games by name
    """
    db_game_list = game_crud.get_game_list_with_search_parameters(
        db=db, offset=offset, limit=limit, search=search)
    return db_game_list


@router.get("/game/genre/{genre_id}", response_model=List[Game], dependencies=[Depends(jwt_scheme)])
def get_game_list_by_genre(genre_id: int, offset: int = 0, limit: int = 50, db: Session = Depends(db_setup.get_db)):
    """
    Get game list by genre

    Parameters:
    - **genre_id**: Genre id
    - **offset**: Skip the first N games (default: 0)
    - **limit**: Limit the number of games returned (default: 50)
    """
    # Get list of game ids by genre id
    db_game_id_list = game_genre_association_crud.get_list_of_game_ids_by_genre_id(
        db=db, genre_id=genre_id, offset=offset, limit=limit)
    
    # Get list of games by game ids
    db_game_list = game_crud.get_game_by_game_id_list(
        db=db, game_id_list=db_game_id_list)
    return db_game_list


@router.get("/game/{id}", response_model=Game, dependencies=[Depends(jwt_scheme)])
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


@router.patch("/game/{id}", response_model=Game, dependencies=[Depends(jwt_scheme)])
def update_game_by_id(id: int, game: GameUpdate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
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

    # Update game genre associations
    game_genre_association_crud.update_associations(
        db=db, game_id=id, updated_association_list=game.genre_list)

    # Update game data
    db_game = game_crud.update_game(db=db, game=game, id=id)

    return db_game


@router.delete("/game/{id}", dependencies=[Depends(jwt_scheme)])
def delete_game_by_id(id: int, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
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

    # Delete game
    game_crud.delete_game(db=db, id=id)

    # Delete game genre associations
    game_genre_association_crud.delete_game_genre_association(
        db=db, game_id=id)

    return {"detail": f"Game with id {id} deleted successfully."}
