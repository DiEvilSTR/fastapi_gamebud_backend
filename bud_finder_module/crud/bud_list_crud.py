from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session

from user_profile_module.schemas.user import UserAsBud
from game_base_module.schemas.game import GameForUserProfileData


def fetch_potential_matches(db: Session, user_id: str):
    """
    Fetch potential matches for user depending on criteria

    Parameters:
    - **db**: Database session
    - **user_id**: User id

    Returns:
    - **db_potential_buds**: List of potential buds
    """
    # Set limits
    first_fetch_limit = 1000  # Adjust the limit as needed for performance
    limit = 50  # Adjust to change the number of potential buds user can see

    # Step 1: Build a query to find potential matches
    custom_query = text(
        """
        WITH user_filters AS (
            SELECT
                :user_id AS user_id,
                (
                    SELECT max_age_preference
                    FROM bud_base_filters
                    WHERE user_id = :user_id
                ) AS user_max_age_preference,
                (
                    SELECT min_age_preference
                    FROM bud_base_filters
                    WHERE user_id = :user_id
                ) AS user_min_age_preference,
                (
                    SELECT country_preference
                    FROM bud_base_filters
                    WHERE user_id = :user_id
                ) AS user_country_preference,
                (
                    SELECT gender
                    FROM users
                    WHERE uuid = :user_id
                ) AS user_gender
        ),
        random_users AS (
            SELECT uuid
            FROM users
            WHERE uuid <> :user_id
            ORDER BY RANDOM()
            LIMIT :first_fetch_limit
        )
        SELECT u.*, (
            SELECT ARRAY(
                SELECT json_build_object('id', uga.game_id, 'name', g.name)
                FROM user_game_association uga
                JOIN games g ON uga.game_id = g.id
                WHERE uga.user_id = u.uuid
            ) AS games
        )
        FROM users u, user_filters uf
        WHERE u.uuid <> :user_id 
            AND AGE(CURRENT_DATE, u.birthday) <= (uf.user_max_age_preference * INTERVAL '1 year')
            AND AGE(CURRENT_DATE, u.birthday) >= (uf.user_min_age_preference * INTERVAL '1 year')
            AND u.country = uf.user_country_preference
            AND u.gender IN (
                SELECT gender_preference
                FROM bud_gender_filters
                WHERE user_id = :user_id
            )
            AND uf.user_gender IN (
                SELECT gender_preference
                FROM bud_gender_filters
                WHERE user_id = u.uuid
            )
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
        ORDER BY RANDOM()
        LIMIT :limit
    """
    )

    db_row_potential_buds = db.execute(custom_query, {
        "user_id": user_id,
        "first_fetch_limit": first_fetch_limit,
        "limit": limit
    }).fetchall()

    # Step 2: Convert rows to UserAsBud objects
    db_potential_buds = [
        UserAsBud(
            uuid=row_bud.uuid,
            nickname=row_bud.nickname,
            age=(
                (datetime.now() - row_bud.birthday).days // 365
            ),
            bio=row_bud.bio,
            gender=row_bud.gender,
            games=[
                GameForUserProfileData(**game) for game in row_bud.games
            ],
            country=row_bud.country)
        for row_bud in db_row_potential_buds
    ]

    return db_potential_buds


# get list of buds who have liked current user
def fetch_list_of_likes_to_user(db: Session, user_id: str):
    """
    Fetch bud list who liked user and match criteria

    Parameters:
    - **db**: Database session
    - **user_id**: User id

    Returns:
    - **db_potential_buds**: List of potential buds
    """
    # Set limits
    limit = 50  # Adjust to change the number of buds who liked him user can see

    # Step 1: Build a query to find potential matches
    custom_query = text(
        """
        WITH user_filters AS (
            SELECT
                :user_id AS user_id,
                (
                    SELECT max_age_preference
                    FROM bud_base_filters
                    WHERE user_id = :user_id
                ) AS user_max_age_preference,
                (
                    SELECT min_age_preference
                    FROM bud_base_filters
                    WHERE user_id = :user_id
                ) AS user_min_age_preference,
                (
                    SELECT country_preference
                    FROM bud_base_filters
                    WHERE user_id = :user_id
                ) AS user_country_preference,
                (
                    SELECT gender
                    FROM users
                    WHERE uuid = :user_id
                ) AS user_gender
        )
        SELECT u.*, (
            SELECT ARRAY(
                SELECT json_build_object('id', uga.game_id, 'name', g.name)
                FROM user_game_association uga
                JOIN games g ON uga.game_id = g.id
                WHERE uga.user_id = u.uuid
            ) AS games
        )
        FROM users u, user_filters uf
        WHERE u.uuid <> :user_id 
            AND AGE(CURRENT_DATE, u.birthday) <= (uf.user_max_age_preference * INTERVAL '1 year')
            AND AGE(CURRENT_DATE, u.birthday) >= (uf.user_min_age_preference * INTERVAL '1 year')
            AND u.country = uf.user_country_preference
            AND u.gender IN (
                SELECT gender_preference
                FROM bud_gender_filters
                WHERE user_id = :user_id
            )
            AND uf.user_gender IN (
                SELECT gender_preference
                FROM bud_gender_filters
                WHERE user_id = u.uuid
            )
            AND u.uuid IN (
                SELECT DISTINCT bl.swiper_id
                FROM bud_likes bl
                WHERE bl.swiped_id = :user_id
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
        ORDER BY RANDOM()
        LIMIT :limit
    """
    )

    db_row_buds_likes = db.execute(custom_query, {
        "user_id": user_id,
        "limit": limit
    }).fetchall()

    # Step 2: Convert rows to UserAsBud objects
    db_potential_buds = [
        UserAsBud(
            uuid=row_bud.uuid,
            nickname=row_bud.nickname,
            age=(
                (datetime.now() - row_bud.birthday).days // 365
            ),
            bio=row_bud.bio,
            gender=row_bud.gender,
            games=[
                GameForUserProfileData(**game) for game in row_bud.games
            ],
            country=row_bud.country)
        for row_bud in db_row_buds_likes
    ]

    return db_potential_buds
