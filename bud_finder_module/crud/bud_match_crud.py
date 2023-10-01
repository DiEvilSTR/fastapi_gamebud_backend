from sqlalchemy.orm import Session

from bud_finder_module.models.bud_match import BudMatch
from bud_finder_module.schemas.bud_match import BudMatchCreate, BudMatchUpdate


def create_match(db: Session, id_one: str, id_two: str):
    """
    Create a new match in the database

    Parameters:
    - **id_one**: First user id
    - **id_two**: Second user id
    """
    db_match = BudMatch(user_one_id=id_one,
                        user_two_id=id_two)
    db.add(db_match)
    db.commit()


def get_match_between_two_buds(db: Session, id_one: str, id_two: str):
    """
    Get match from the database

    Parameters:
    - **id_one**: First user id
    - **id_two**: Second user id
    """
    return db.query(BudMatch).filter(
        BudMatch.user_one_id == id_one,
        BudMatch.user_two_id == id_two
    ).first()


def get_match_by_id(db: Session, id: int):
    """
    Get match from the database

    Parameters:
    - **id**: Match id
    """
    return db.query(BudMatch).filter(BudMatch.id == id).first()


def get_all_matches_for_user(db: Session, id: str):
    """
    Get all matches for user

    Parameters:
    - **id**: User id
    """
    return db.query(BudMatch).filter(
        (BudMatch.user_one_id == id) | (BudMatch.user_two_id == id)
    ).all()


def delete_match_by_match_id(db: Session, id: int):
    """
    Delete match from the database

    Parameters:
    - **id**: Match id
    """
    db_match = db.query(BudMatch).filter(BudMatch.id == id).first()
    db.delete(db_match)
    db.commit()


def delete_match_by_user_id(db: Session, bud_id: str):
    """
    Delete all matches for user from the database

    Parameters:
    - **id**: User id
    """
    db.query(BudMatch).filter(
        (BudMatch.user_one_id == bud_id) | (BudMatch.user_two_id == bud_id)
    ).delete(synchronize_session=False)
    db.commit()