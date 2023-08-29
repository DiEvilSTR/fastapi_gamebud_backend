from decouple import config
from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from user_profile_module.models.user import User
from user_profile_module.schemas.user import UserCreate, UserUpdate
from user_profile_module.schemas.auth import UserLogin


# 1 Read User [Get user by uuid]
def get_user_by_uuid(db: Session, uuid: str):
    return db.query(User).filter(User.uuid == uuid).first()


# 2 Read User [Get user by email]
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# 3 Create User [Create user]
def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email,
                   hashed_password=hashed_password,
                   nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 4 Delete User [Delete user]
def delete_user(db: Session, email: str):
    db_user = get_user_by_email(db=db, email=email)
    db.delete(db_user)
    db.commit()
    return db_user


# 5 Update User [Update user]
def update_user(db: Session, user: UserUpdate, email: str):
    db_user = get_user_by_email(db=db, email=email)
    updated_user = user.dict(exclude_unset=True)
    for key, value in updated_user.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 6 Authenticate User [Authenticate user]
def authenticate(db: Session, user: UserLogin):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user and verify_password(user.password, db_user.hashed_password):
        return True
    else:
        return None
