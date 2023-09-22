from decouple import config
from sqlalchemy.orm import Session
from typing import List

from user_profile_module.models.user_game_association import UserGameAssociation


def get_association_by_game_id(db: Session, game_id: int):
    """
    Get user-game association by game id

    Parameters:
    - **game_id**: Game id
    """
    return db.query(UserGameAssociation).filter(UserGameAssociation.game_id == game_id).first()


def add_user_game_association(db: Session, user_id: str, games_list: List[int]):
    """
    Add associations

    Parameters:
    - **user_id**: User id
    - **games_list**: List of games ids
    """
    db_association_list = []
    for game_id in games_list:
        db_association = UserGameAssociation(user_id=user_id,
                                             game_id=game_id)
        db_association_list.append(db_association)
    db.bulk_save_objects(db_association_list)
    db.commit()


def delete_user_game_association(db: Session, game_id: int = None, user_id: str = None):
    """
    Delete user-game associations

    Parameters:
    - **game_id**: Game id
    - **user_id**: User id
    """
    filter_conditions = []

    if game_id is not None:
        filter_conditions.append(UserGameAssociation.game_id == game_id)

    if user_id is not None:
        filter_conditions.append(UserGameAssociation.user_id == user_id)

    db.query(UserGameAssociation).filter(
        *filter_conditions).delete(synchronize_session=False)
    db.commit()


def update_associations(db: Session, user_id: str, updated_association_list: List[int]):
    """
    Update associations

    Parameters:
    - **user_id**: User id
    - **updated_association_list**: List of games ids
    """
    db_user_game_associations = db.query(UserGameAssociation).filter(
        UserGameAssociation.user_id == user_id).all()
    current_game_ids = [
        association.game_id for association in db_user_game_associations]
    updated_game_ids = updated_association_list

    # Delete associations
    for game_id in current_game_ids:
        if game_id not in updated_game_ids:
            delete_user_game_association(
                db=db, game_id=game_id, user_id=user_id)

    # Add associations
    for game_id in updated_game_ids:
        if game_id not in current_game_ids:
            add_user_game_association(db=db, user_id=user_id,
                                      games_list=[game_id])

    db.commit()
