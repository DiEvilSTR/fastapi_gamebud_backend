from decouple import config
from sqlalchemy.orm import Session

from game_base_module.models.association import GameGenreAssociation
from game_base_module.schemas.association import GameGenreAssociationCreate


# 1 Read association by game id [Get association by game id]
def get_association_by_game_id(db: Session, game_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.game_id == game_id).first()


# 2 Read association by game genre id [Get association by genre id]
def get_game_genre_by_name(db: Session, genre_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.genre_id == genre_id).first()


# 3 Read certain association [Get certain association]
def get_certain_association(db: Session, game_id: int, genre_id: int):
    return db.query(GameGenreAssociation).filter(GameGenreAssociation.game_id == game_id,
                                                 GameGenreAssociation.genre_id == genre_id).first()


# 4 Add association [Add association]
def add_association(db: Session, association: GameGenreAssociation):
    db_association = GameGenreAssociation(game_id=association.game_id,
                                          genre_id=association.genre_id)
    db.add(db_association)
    db.commit()
    db.refresh(db_association)
    return db_association


# 5 Delete game genre association [Delete game genre]
def delete_game_genre_association(db: Session, game_id: int, genre_id: int):
    db_game_genre = get_certain_association(
        db=db, game_id=game_id, genre_id=genre_id)
    db.delete(db_game_genre)
    db.commit()
    return db_game_genre
