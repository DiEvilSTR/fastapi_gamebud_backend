import random
from datetime import datetime, timedelta

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from user_profile_module import User
from bud_finder_module import BudLike, BudMatch


"""
        AND u.uuid NOT IN (
            SELECT DISTINCT bl.swiped_id
            FROM bud_likes bl
            WHERE bl.swiper_id = :user_id
        )
        AND u.uuid NOT IN (
            SELECT DISTINCT bm.user_one_id
            FROM bud_matches bm
            WHERE bm.user_two_id = :user_id
            UNION
            SELECT DISTINCT bm.user_two_id
            FROM bud_matches bm
            WHERE bm.user_one_id = :user_id
        )
        AND u.birthday >= :min_birthdate
        AND u.birthday <= :max_birthdate
        AND EXISTS (
            SELECT 1
            FROM user_game_association uga
            WHERE uga.user_id = u.uuid
                AND uga.game_id IN (
                    SELECT game_id
                    FROM user_game_association
                    WHERE user_id = :user_id
                )
        )
"""


def find_potential_matches(db: Session, min_age: int, max_age: int, user_id: str):
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
    # Set offset and limit
    limit = 50

    # Step 1: Get list of user's games
    db_user_games = db.query(User).filter(User.uuid == user_id).first().games
    db_user_games_ids = [game.id for game in db_user_games]

    # Step 2: Get list of users that have been liked or matched
    # db_liked_users = db.query(BudLike).filter(
    #     BudLike.swiper_id == user_id).all()
    # db_liked_users_ids = [bud.swiped_id for bud in db_liked_users]

    # db_matched_users_as_user_one = db.query(BudMatch).filter(
    #     BudMatch.user_one_id == user_id).all()
    # db_matched_users_as_user_two = db.query(BudMatch).filter(
    #     BudMatch.user_two_id == user_id).all()
    # db_matched_users_ids = [bud.user_one_id for bud in db_matched_users_as_user_two] + [
    #     bud.user_two_id for bud in db_matched_users_as_user_one]

    # db_liked_and_matched_users_ids = db_liked_users_ids + db_matched_users_ids
    # ids_to_exclude = db_liked_and_matched_users_ids + [user_id]

    # Ster 3: Calculate birthdate for minimum and maximum ages
    min_birthdate = datetime.now() - timedelta(days=(min_age * 365))
    max_birthdate = datetime.now() - timedelta(days=(max_age * 365))

    # Step 4: Build a query to find potential matches
    custom_query = text("""
    SELECT u.*
    FROM users u
    WHERE u.uuid <> :user_id
    AND u.birthday >= :min_birthdate
    AND u.birthday <= :max_birthdate
    ORDER BY RANDOM()
    LIMIT :limit
    """)

    db_potential_buds = db.execute(custom_query, {
        "user_id": user_id,
        "min_birthdate": min_birthdate,
        "max_birthdate": max_birthdate,
        "limit": limit
    }).fetchall()

    # Step 3: Build a query to find potential matches
    # db_potential_buds = db.query(User).filter(
    #     User.uuid.notin_(ids_to_exclude),
    #     User.birthday >= min_birthdate,
    #     User.birthday <= max_birthdate
    # ).order_by(func.random()).offset(offset).limit(limit).all()

    # Step 4: Calculate age
    # for bud in db_potential_buds:
    #     bud.age = bud.count_age

    return db_potential_buds
