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


# 1 Add game genre [Add a new game genre to the database]
@router.post("/game_genre", response_model=GameGenre, status_code=status.HTTP_201_CREATED)
def add_new_game_genre(game_genre: GameGenreCreate, db: Session = Depends(db_setup.get_db)):
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


# 2 Read game genre list [Get game genre list]
@router.get("/game_genre", response_model=List[GameGenreForList])
def get_game_genre_list(skip: int = 0, limit: int = 100, db: Session = Depends(db_setup.get_db)):
    db_game_genre_list = game_genre_crud.get_game_genre_list(
        db=db, skip=skip, limit=limit)
    return db_game_genre_list


# 3 Read game genre [Get game genre by id]
@router.get("/game_genre/{id}", response_model=GameGenre)
def get_game_genre_by_id(id: int, db: Session = Depends(db_setup.get_db)):
    db_game_genre = game_genre_crud.get_game_genre_by_id(db=db, id=id)
    if db_game_genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game genre with this id does not exists."
        )
    return db_game_genre


# 4 Update game genre [Update game genre]
@router.patch("/game_genre/{id}", response_model=GameGenre)
def update_game_genre(id: int, game_genre: GameGenreUpdate, db: Session = Depends(db_setup.get_db)):
    db_game_genre = game_genre_crud.get_game_genre_by_id(db=db, id=id)
    if db_game_genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game genre with this id does not exists."
        )
    db_game_genre = game_genre_crud.update_game_genre(
        db=db, game_genre=game_genre, id=id)
    return db_game_genre


# 2 Add game [Add a new game to the database]
@router.post("/game", response_model=Game, status_code=status.HTTP_201_CREATED)
def add_new_game(game: GameCreate, db: Session = Depends(db_setup.get_db)):
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


# # 4 Read current user [Get current user]
# @router.get("/me", response_model=User, dependencies=[Depends(jwt_scheme)])
# def read_current_user(db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
#     db_user = user_crud.get_user_by_email(
#         db=db, email=current_user_email)
#     if db_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
#         )
#     return db_user


# # 5 Update User Profile [Update user profile]
# @router.patch("/me", response_model=User, dependencies=[Depends(jwt_scheme)])
# def update_current_user(updated_user: UserUpdate, db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
#     db_user = user_crud.get_user_by_email(
#         db=db, email=current_user_email)
#     if db_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
#         )
#     db_user = user_crud.update_user(
#         db=db, user=updated_user, email=current_user_email)
#     return db_user


# # 6 Delete User [Delete user, user profile, and all user's tasks]
# @router.delete("/me", dependencies=[Depends(jwt_scheme)])
# def delete_current_user(response: Response, db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
#     db_user = user_crud.get_user_by_email(db=db, email=current_user_email)
#     if db_user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
#         )
#     user_crud.delete_user(db=db, email=current_user_email)
#     response.delete_cookie(key="Authorization")
#     return {"detail": f"User with email {current_user_email} deleted successfully."}
