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

router = APIRouter()


@router.post("/login", response_model=Token)
def user_login(user: UserLogin, db: Session = Depends(db_setup.get_db)):
    """
    User login

    Parameters:
    - **user**: User login details
    """
    db_user = user_crud.authenticate(db=db, user=user)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid login details!"
        )
    
    if db_user.is_active is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is inactive. Please contact the admin."
        )
    else:
        return jwt_handler.sign_jwt(db_user.uuid)


@router.post("/logout", dependencies=[Depends(jwt_scheme)])
def user_logout(response: Response):
    """
    User logout
    """
    response.delete_cookie(key="Authorization")
    return {"detail": "Successfully logged out!"}


@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserCreate, db: Session = Depends(db_setup.get_db)):
    """
    User signup

    Parameters:
    - **user**: User signup details
    """
    db_user = user_crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is already registered. Please try another one."
        )
    db_user = user_crud.create_user(db=db, user=user)
    return db_user


@router.get("/me", response_model=User, dependencies=[Depends(jwt_scheme)])
def read_current_user(db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    """
    Get current user
    """
    db_user = user_crud.get_user_by_email(
        db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
        )
    return db_user


@router.get("/me/update", response_model=UserInDBForUpdate, dependencies=[Depends(jwt_scheme)])
def read_current_user_for_update(db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    """
    Get current user for update
    """
    db_user = user_crud.get_user_by_email_for_update(
        db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
        )
    return db_user


@router.patch("/me/update", response_model=User, dependencies=[Depends(jwt_scheme)])
def update_current_user(updated_user: UserUpdate, db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    """
    Update current user

    Parameters:
    - **updated_user**: Updated user data
    """
    db_user = user_crud.get_user_by_email_for_update(
        db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
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
        db=db, user=updated_user, email=current_user_email)
    return db_user


@router.delete("/me/delete", dependencies=[Depends(jwt_scheme)])
def delete_current_user(response: Response, db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    """
    Delete current user
    """
    db_user = user_crud.get_user_by_email(db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
        )

    # Delete user
    user_crud.delete_user(db=db, email=current_user_email)

    # Delete user-game associations
    user_game_association_crud.delete_user_game_association(
        db=db, user_id=db_user.uuid)

    # Delete cookie
    response.delete_cookie(key="Authorization")
    return {"detail": f"User with email {current_user_email} deleted successfully."}
