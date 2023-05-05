from decouple import config
from sqlalchemy.orm import Session

from core.security import verify_password
from models.user import User
from schemas.auth import UserLogin


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def authenticate(db: Session, user: UserLogin):
    db_user = get_user(db=db, username=user.username)
    if db_user and verify_password(user.password, db_user.hashed_password):
        return True
    else:
        return None
