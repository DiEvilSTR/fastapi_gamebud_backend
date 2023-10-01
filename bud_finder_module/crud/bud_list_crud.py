from sqlalchemy.orm import Session

from user_profile_module import User
from bud_finder_module import BudLike, BudMatch


def read_list_of_users(db: Session, offset: int, limit: int):
    """
    Get list of new users

    Parameters:
    - **offset**: Offset
    - **limit**: Limit
    """
    return db.query(User).filter().offset(offset).limit(limit).all()