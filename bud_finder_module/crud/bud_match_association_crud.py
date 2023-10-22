from sqlalchemy.orm import Session
from bud_finder_module.models.bud_match_association import BudMatchAssociation

def create_bud_match_associations(db: Session, user_id_1: str, user_id_2: str, match_id: int):
    """
    Create bud match associations
    
    Parameters:
    - **db**: Database session
    - **user_id_1**: User id 1 (string UUID)
    - **user_id_2**: User id 2 (string UUID)
    - **match_id**: Match id (integer)
    """
    association_1 = BudMatchAssociation(user_id=user_id_1, match_id=match_id)
    association_2 = BudMatchAssociation(user_id=user_id_2, match_id=match_id)
    db.add(association_1)
    db.add(association_2)
    db.commit()


def delete_bud_match_associations(db: Session, matches_ids_list: int):
    """
    Delete bud match associations
    
    Parameters:
    - **db**: Database session
    - **matches_ids_list**: Match id (list of integers)
    """
    db.query(BudMatchAssociation).filter(BudMatchAssociation.match_id.in_(matches_ids_list)).delete(synchronize_session=False)
    db.commit()


def get_bud_matches_ids(db: Session, user_id: str):
    """
    Get bud matches ids
    
    Parameters:
    - **db**: Database session
    - **user_id**: User id (string UUID)
    """
    # Get list of matches
    db_matches = db.query(BudMatchAssociation).filter(BudMatchAssociation.user_id == user_id).all()
    
    # Get list of matches ids
    db_matches_ids = [db_match.match_id for db_match in db_matches]
    
    return db_matches_ids