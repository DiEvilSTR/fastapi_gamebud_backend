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


@router.get("/list")
def fetch_bud_list(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get list of new users

    Parameters:
    - **offset**: Offset
    - **limit**: Limit
    """
    return bud_list_crud.find_potential_matches(db=db, user_id=current_user_id, min_age=18, max_age=100)
