from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from user_profile_module.models.user import User
from user_profile_module.schemas.user import UserCreate, UserUpdate
from user_profile_module.schemas.auth import UserLogin


def get_user_by_uuid(db: Session, uuid: str):
    """
    Get user by uuid. For future use.

    Parameters:
    - **uuid**: User uuid
    """
    db_user = db.query(User).filter(User.uuid == uuid).first()

    if db_user is None:
        return None

    # Calculate user's age
    db_user.age = db_user.count_age
    return db_user


def get_user_by_email(db: Session, email: str):
    """
    Get user by email

    Parameters:
    - **email**: User email
    """
    db_user = db.query(User).filter(User.email == email).first()

    if db_user is None:
        return None

    # Calculate user's age
    db_user.age = db_user.count_age
    return db_user


def get_user_by_uuid_for_update(db: Session, uuid: str):
    """
    Get user by email for update

    Parameters:
    - **uuid**: User uuid
    """
    return db.query(User).filter(User.uuid == uuid).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database

    Parameters:
    - **user**: User data to be added
    """
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email,
                   hashed_password=hashed_password,
                   birthday=user.birthday,
                   nickname=user.nickname,
                   gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Calculate user's age
    db_user.age = db_user.count_age
    return db_user


def update_user(db: Session, user: UserUpdate, uuid: str):
    """
    Update user in the database

    Parameters:
    - **user**: User data to be updated
    - **uuid**: User uuid
    """
    db_user = get_user_by_uuid_for_update(db=db, uuid=uuid)
    updated_user = user.model_dump(exclude_unset=True)

    # Get the list of model attributes
    model_attributes = db_user.__table__.columns.keys()

    for key, value in updated_user.items():
        if key in model_attributes:
            setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Calculate user's age
    db_user.age = db_user.count_age
    return db_user


def delete_user(db: Session, uuid: str):
    """
    Delete user from the database

    Parameters:
    - **uuid**: User uuid
    """
    db_user = get_user_by_uuid(db=db, uuid=uuid)
    db.delete(db_user)
    db.commit()
    return db_user


def authenticate(db: Session, user: UserLogin):
    """
    Authenticate user

    Parameters:
    - **user**: User login details
    """
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user and verify_password(user.password, db_user.hashed_password):
        return db_user
    else:
        return None
