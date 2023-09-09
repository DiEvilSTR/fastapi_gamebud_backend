from decouple import config
from sqlalchemy.orm import Session
from typing import List

from game_base_module.models.association import GameGenreAssociation
from game_base_module.schemas.association import GameGenreAssociationCreate


# 1 Read association by game id [Get association by game id]
def get_association_by_game_id(db: Session, game_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.game_id == game_id).first()


# 2 Read association by game genre id [Get association by genre id]
def get_game_genre_by_name(db: Session, genre_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.genre_id == genre_id).first()


# 3 Count associated games by genre id [Count associated games by genre id]
def count_associated_games_by_genre_id(db: Session, genre_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.genre_id == genre_id).count()


# 4 Read certain association [Get certain association]
def get_certain_association(db: Session, game_id: int, genre_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.game_id == game_id,
                                                 GameGenreAssociation.genre_id == genre_id).first()


# 5 Add associations [Add associations]
def add_association(db: Session, game_id: int, association_list: List[int]):
    db_association_list = []
    for associated_game_genre in association_list:
        db_association = GameGenreAssociation(game_id=game_id,
                                              genre_id=associated_game_genre)
        db_association_list.append(db_association)
    db.bulk_save_objects(db_association_list)
    db.commit()


# 6 Delete game genre associations [Delete game genre]
def delete_game_genre_association(db: Session, game_id: int, genre_ids: List[int]):
    db.query(GameGenreAssociation).filter(
        GameGenreAssociation.game_id == game_id,
        GameGenreAssociation.genre_id.in_(genre_ids)
    ).delete(synchronize_session=False)
    db.commit()
