from sqlalchemy.orm import Session
from typing import List

from bud_finder_module.models.bud_match import BudMatch
from bud_finder_module.schemas.bud_match import BudMatchCreate


def fetch_matches(db: Session, matches_ids_list: List[int]):
    """
    Fetch matches for user

    Parameters:
    - **user_id**: User id
    """
    # Get list of matches ids
    
    return db.query(BudMatch).filter(BudMatch.id.in_(matches_ids_list)).all()


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
    db.query(BudMatch).filter(BudMatch.id.in_(matches_ids_list)).delete(synchronize_session=False)
    db.commit()
