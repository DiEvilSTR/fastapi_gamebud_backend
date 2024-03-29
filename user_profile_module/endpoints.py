from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme
from core.jwt_authentication import jwt_handler

from user_profile_module.crud import user_crud
from user_profile_module.crud import user_game_association_crud
from user_profile_module.schemas.auth import Token, UserLogin
from user_profile_module.schemas.user import User, UserCreate, UserUpdate, UserInDBForUpdate

# Imports from other modules
from bud_finder_module.crud import bud_like_crud, bud_match_crud, bud_match_association_crud


router = APIRouter()


@router.post("/login", response_model=User)
def user_login(user: UserLogin, response: Response, db: Session = Depends(db_setup.get_db)):
    """
    User login

    Parameters:
    - **user**: User login details

    Returns:
    - **Token**: JWT token
    """
    db_user: User = user_crud.authenticate(db=db, user=user)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid login details!"
        )

    if db_user.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is inactive. Please contact the admin."
        )

    else:
        jwt_handler.set_cookie_jwt(response=response, uuid=db_user.uuid)
        return db_user


@router.post("/logout", dependencies=[Depends(jwt_scheme)])
def user_logout(response: Response):
    """
    User logout
    """
    response.delete_cookie(key="Authorization")
    return {"detail": "Successfully logged out!"}


@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserCreate, response: Response, db: Session = Depends(db_setup.get_db)):
    """
    User signup

    Parameters:
    - **user**: User signup details

    Returns:
    - **Token**: JWT token
    """
    db_user: User = user_crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is already registered. Please try another one."
        )
    db_user = user_crud.create_user(db=db, user=user)

    jwt_handler.set_cookie_jwt(response=response, uuid=db_user.uuid)


@router.get("/me", response_model=User, dependencies=[Depends(jwt_scheme)])
def read_current_user(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get current user

    Returns:
    - **User**: User data
    """
    db_user = user_crud.get_user_by_uuid(
        db=db, uuid=current_user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this uuid does not exists."
        )
    return db_user


@router.get("/me/update", response_model=UserInDBForUpdate, dependencies=[Depends(jwt_scheme)])
def read_current_user_for_update(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get current user for update

    Returns:
    - **UserInDBForUpdate**: User data for update
    """
    db_user = user_crud.get_user_by_uuid_for_update(
        db=db, uuid=current_user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this uuid does not exists."
        )
    return db_user


@router.patch("/me/update", response_model=User, dependencies=[Depends(jwt_scheme)])
def update_current_user(updated_user: UserUpdate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Update current user

    Parameters:
    - **updated_user**: Updated user data

    Returns:
    - **User**: Updated user data
    """
    db_user = user_crud.get_user_by_uuid_for_update(
        db=db, uuid=current_user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this uuid does not exists."
        )

    if updated_user.games:
        # Check updated_user games list length is less than or equal to 5
        if len(updated_user.games) > 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User can choose maximum 5 games."
            )

        # Update user-game associations
        user_game_association_crud.update_associations(
            db=db, user_id=db_user.uuid, updated_association_list=updated_user.games)

    # Update user data
    db_user = user_crud.update_user(
        db=db, user=updated_user, uuid=current_user_id)
    return db_user


@router.delete("/me/delete", dependencies=[Depends(jwt_scheme)])
def delete_current_user(response: Response, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Delete current user
    """
    db_user = user_crud.get_user_by_uuid(db=db, uuid=current_user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this uuid does not exists."
        )

    # Delete user-game associations
    user_game_association_crud.delete_user_game_association(
        db=db, user_id=db_user.uuid)

    # Delete bud likes
    bud_like_crud.delete_likes_for_user(db=db, user_id=current_user_id)

    # Delete bud matches
    db_matched_ids = bud_match_association_crud.get_bud_matches_ids(
        db=db, user_id=current_user_id)
    bud_match_association_crud.delete_bud_match_associations(
        db=db, matches_ids_list=db_matched_ids)
    bud_match_crud.delete_matches_from_matches_ids_list(
        db=db, matches_ids_list=db_matched_ids)

    # Delete user
    user_crud.delete_user(db=db, uuid=current_user_id)

    # Delete cookie
    response.delete_cookie(key="Authorization")
    return {"detail": "User deleted successfully."}


# Get number of registered users
@router.get("/count", response_model=int)
def get_number_of_registered_users(db: Session = Depends(db_setup.get_db)):
    """
    Get number of registered users

    Returns:
    - **users_count**: Number of registered users in the database (int)
    """
    users_count = user_crud.get_number_of_registered_users(db=db)

    return users_count
