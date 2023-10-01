from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme

from bud_finder_module.crud import bud_like_crud, bud_match_crud, bud_list_crud
from bud_finder_module.schemas.bud_like import BudLikeCreate, BudDislikeCreate
from bud_finder_module.schemas.bud_match import BudMatchCreate
from user_profile_module.schemas.user import User

router = APIRouter()

# Game genre endpoints


@router.get("/list", response_model=List[User])
def fetch_bud_list(offset: int = 0, limit: int = 10, db: Session = Depends(db_setup.get_db)):
    """
    Get list of new users

    Parameters:
    - **offset**: Offset
    - **limit**: Limit
    """
    return bud_list_crud.read_list_of_users(db, offset, limit)