import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from user_profile_module import User
from bud_finder_module import BudLike, BudMatch


def find_potential_matches(db: Session, min_age: int, max_age: int, user_id: str, offset: int, limit: int):
    """
    Find potential matches for user depending on criteria

    Parameters:
    - **db**: Database session
    - **min_age**: Minimum age chosen by user
    - **max_age**: Maximum age chosen by user
    - **user_id**: User id
    - **offset**: Offset
    - **limit**: Limit

    Returns:
    - **db_potential_buds**: List of potential buds
    """
    # Step 1: Get list of user's games
    db_user_games = db.query(User).filter(User.uuid == user_id).first().games

    # Step 2: Get list of users that have been liked or matched
    db_liked_users = db.query(BudLike).filter(
        BudLike.swiper_id == user_id).all()
    db_liked_users_ids = [bud.swiped_id for bud in db_liked_users]

    db_matched_users_as_user_one = db.query(BudMatch).filter(
        BudMatch.user_one_id == user_id).all()
    db_matched_users_as_user_two = db.query(BudMatch).filter(
        BudMatch.user_two_id == user_id).all()
    db_matched_users_ids = [bud.user_one_id for bud in db_matched_users_as_user_two] + [
        bud.user_two_id for bud in db_matched_users_as_user_one]

    db_liked_and_matched_users_ids = db_liked_users_ids + db_matched_users_ids
    ids_to_exclude = db_liked_and_matched_users_ids + [user_id]

    # Ster 3: Calculate birthdate for minimum and maximum ages
    min_birthdate = datetime.now() - timedelta(days=(min_age * 365))
    max_birthdate = datetime.now() - timedelta(days=(max_age * 365))

    # Step 3: Build a query to find potential matches
    db_potential_buds = db.query(User).filter(
        User.uuid.notin_(ids_to_exclude),
        User.birthday >= min_birthdate,
        User.birthday <= max_birthdate
    ).order_by(func.random()).offset(offset).limit(limit).all()

    # Step 4: Calculate age
    for bud in db_potential_buds:
        bud.age = bud.count_age

    return db_potential_buds
