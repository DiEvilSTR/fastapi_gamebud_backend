from decouple import config
from sqlalchemy.orm import Session

from game_base_module.models.game import Game
from game_base_module.schemas.game import GameCreate, GameUpdate


# 1 Read Game [Get game by id]
def get_game_by_id(db: Session, id: str):
    return db.query(Game).filter(Game.id == id).first()


# 2 Read Game [Get game by name]
def get_game_by_name(db: Session, name: str):
    return db.query(Game).filter(Game.name == name).first()


# 3 Read Game List [Get game list]
def get_game_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Game).offset(skip).limit(limit).all()


# 4 Add Game [Create game]
def add_game(db: Session, game: GameCreate):
    db_game = Game(name=game.name,
                   description=game.description)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game.id


# 5 Update Game [Update game]
def update_game(db: Session, game: GameUpdate, id: int):
    db_game = get_game_by_id(db=db, id=id)
    updated_user = game.model_dump(exclude_unset=True)
    for key, value in updated_user.items():
        setattr(db_game, key, value)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


# 6 Delete Game [Delete game]
def delete_user(db: Session, id: int):
    db_game = get_game_by_id(db=db, id=id)
    db.delete(db_game)
    db.commit()
    return db_game
