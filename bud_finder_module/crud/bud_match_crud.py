from sqlalchemy.orm import Session
from typing import List

from bud_finder_module.models.bud_match import BudMatch
from bud_finder_module.schemas.bud_match import BudMatchCreate, BudMatchForMatchList
from user_profile_module.schemas.user import UserAsBudForMatchList


def fetch_matches(db: Session, matches_ids_list: List[int]):
    """
    Fetch matches for user

    Parameters:
    - **user_id**: User id
    """
    return db.query(BudMatch).filter(BudMatch.id.in_(matches_ids_list)).all()


def fetch_matches_for_user(db: Session, user_id: str, matches_ids_list: List[int]):
    """
    Fetch matches for user and return matches list

    Parameters:
    - **id**: Match id
    - **bud**: Opponent user id
    """
    db_matches: List[BudMatch] = db.query(BudMatch).filter(
        BudMatch.id.in_(matches_ids_list)).all()
    matches_list: List[BudMatchForMatchList] = []

    for db_match in db_matches:
        db_match_bud_1: UserAsBudForMatchList = db_match.buds[0]
        db_match_bud_2: UserAsBudForMatchList = db_match.buds[1]
        if db_match_bud_1.uuid == user_id:
            matches_list.append(BudMatchForMatchList(
                id=db_match.id, bud=db_match_bud_2))
        else:
            matches_list.append(BudMatchForMatchList(
                id=db_match.id, bud=db_match_bud_1))

    return matches_list


def create_match(db: Session):
    """
    Create a new match in the database

    Returns:
    - **db_match.id**: Match id
    """
    db_match = BudMatch()
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match.id


def get_match_by_match_id(db: Session, match_id: int) -> BudMatch:
    """
    Get match from the database

    Parameters:
    - **match_id**: Match id
    """
    return db.query(BudMatch).filter(BudMatch.id == match_id).first()


def delete_matches_from_matches_ids_list(db: Session, matches_ids_list: List[int]):
    """
    Delete match from the database

    Parameters:
    - **matches_ids_list**: Match id
    """
    db.query(BudMatch).filter(BudMatch.id.in_(
        matches_ids_list)).delete(synchronize_session=False)
    db.commit()
