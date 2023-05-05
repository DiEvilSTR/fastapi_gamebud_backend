from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.jwt_authentication.jwt_bearer import jwt_scheme
from crud import crud_user
from db.db_setup import get_db
from schemas.user import User

router = APIRouter()


#1 Read Users [Get list of users]
@router.get("/", response_model=List[User], dependencies=[Depends(jwt_scheme)])
def read_user(db: Session = Depends(get_db), current_user: str = Depends(jwt_scheme)):
    db_user = crud_user.get_user(db, username=current_user)
    return db_user
