from decouple import config
from sqlalchemy.orm import Session
from typing import List

from game_base_module.models.association import GameGenreAssociation


def get_association_by_game_id(db: Session, game_id: int):
    """
    Get association by game id

    Parameters:
    - **game_id**: Game id
    """
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.game_id == game_id).first()


def get_game_genre_by_name(db: Session, genre_id: int):
    """
    Get association by genre id

    Parameters:
    - **genre_id**: Genre id
    """
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.genre_id == genre_id).first()


def count_associated_games_by_genre_id(db: Session, genre_id: int):
    """
    Count associated games by genre id

    Parameters:
    - **genre_id**: Genre id
    """
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.genre_id == genre_id).count()


def get_certain_association(db: Session, game_id: int, genre_id: int):
    """
    Get certain association

    Parameters:
    - **game_id**: Game id
    - **genre_id**: Genre id
    """
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.game_id == game_id,
                                                 GameGenreAssociation.genre_id == genre_id).first()


def add_association(db: Session, game_id: int, association_list: List[int]):
    """
    Add associations

    Parameters:
    - **game_id**: Game id
    - **association_list**: List of genre ids
    """
    db_association_list = []
    for associated_game_genre in association_list:
        db_association = GameGenreAssociation(game_id=game_id,
                                              genre_id=associated_game_genre)
        db_association_list.append(db_association)
    db.bulk_save_objects(db_association_list)
    db.commit()


def delete_game_genre_association(db: Session, game_id: int = None, genre_id: int = None):
    """
    Delete game genre associations

    Parameters:
    - **game_id**: Game id
    - **genre_id**: Genre id
    """
    filter_conditions = []

    if game_id is not None:
        filter_conditions.append(GameGenreAssociation.game_id == game_id)

    if genre_id is not None:
        filter_conditions.append(GameGenreAssociation.genre_id == genre_id)

    db.query(GameGenreAssociation).filter(
        *filter_conditions).delete(synchronize_session=False)
    db.commit()


def update_associations(db: Session, game_id: int, updated_association_list: List[int]):
    """
    Update associations

    Parameters:
    - **game_id**: Game id
    - **updated_association_list**: List of genre ids
    """
    db_game_genre_associations = db.query(GameGenreAssociation).filter(
        GameGenreAssociation.game_id == game_id).all()
    current_genre_ids = [
        association.genre_id for association in db_game_genre_associations]
    updated_genre_ids = updated_association_list

    # Delete associations
    for genre_id in current_genre_ids:
        if genre_id not in updated_genre_ids:
            delete_game_genre_association(
                db=db, game_id=game_id, genre_id=genre_id)

    # Add associations
    for genre_id in updated_genre_ids:
        if genre_id not in current_genre_ids:
            add_association(db=db, game_id=game_id,
                            association_list=[genre_id])

    db.commit()
