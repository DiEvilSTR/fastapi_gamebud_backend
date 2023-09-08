from decouple import config
from sqlalchemy.orm import Session

from game_base_module.models.game_genre import GameGenre
from game_base_module.schemas.game_genre import GameGenreCreate, GameGenreUpdate


# 1 Read game genre [Get game genre by id]
def get_game_genre_by_id(db: Session, id: str):
    return db.query(GameGenre).filter(GameGenre.id == id).first()


# 2 Read game genre [Get game genre by name]
def get_game_genre_by_name(db: Session, name: str):
    return db.query(GameGenre).filter(GameGenre.name == name).first()


# 3 Read game genre list [Get game genre list]
def get_game_genre_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GameGenre).offset(skip).limit(limit).all()


# 4 Add game genre [Add game genre]
def add_game_genre(db: Session, game_genre: GameGenreCreate):
    db_game_genre = GameGenre(name=game_genre.name,
                              description=game_genre.description)
    db.add(db_game_genre)
    db.commit()
    db.refresh(db_game_genre)
    return db_game_genre


# 5 Update game genre [Update game genre]
def update_game_genre(db: Session, game_genre: GameGenreUpdate, id: int):
    db_game_genre = get_game_genre_by_id(db=db, id=id)
    updated_game_genre = game_genre.model_dump(exclude_unset=True)
    for key, value in updated_game_genre.items():
        setattr(db_game_genre, key, value)
    db.add(db_game_genre)
    db.commit()
    db.refresh(db_game_genre)
    return db_game_genre


# 6 Delete game genre [Delete game genre]
def delete_game_genre(db: Session, id: int):
    db_game_genre = get_game_genre_by_id(db=db, id=id)
    db.delete(db_game_genre)
    db.commit()
    return db_game_genre
