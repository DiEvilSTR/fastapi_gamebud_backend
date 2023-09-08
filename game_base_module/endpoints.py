from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme
from core.jwt_authentication import jwt_handler

from user_profile_module.crud import user_crud
from user_profile_module.schemas.auth import Token, UserLogin
from user_profile_module.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


# 1 Create  [Create a new user]
@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
def user_signup(user: UserCreate, db: Session = Depends(db_setup.get_db)):
    db_user = user_crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is already registered. Please try another one."
        )
    db_user = user_crud.create_user(db=db, user=user)
    return db_user


# 4 Read current user [Get current user]
@router.get("/me", response_model=User, dependencies=[Depends(jwt_scheme)])
def read_current_user(db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    db_user = user_crud.get_user_by_email(
        db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
        )
    return db_user


# 5 Update User Profile [Update user profile]
@router.patch("/me", response_model=User, dependencies=[Depends(jwt_scheme)])
def update_current_user(updated_user: UserUpdate, db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    db_user = user_crud.get_user_by_email(
        db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
        )
    db_user = user_crud.update_user(
        db=db, user=updated_user, email=current_user_email)
    return db_user


# 6 Delete User [Delete user, user profile, and all user's tasks]
@router.delete("/me", dependencies=[Depends(jwt_scheme)])
def delete_current_user(response: Response, db: Session = Depends(db_setup.get_db), current_user_email: str = Depends(jwt_scheme)):
    db_user = user_crud.get_user_by_email(db=db, email=current_user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exists."
        )
    user_crud.delete_user(db=db, email=current_user_email)
    response.delete_cookie(key="Authorization")
    return {"detail": f"User with email {current_user_email} deleted successfully."}
