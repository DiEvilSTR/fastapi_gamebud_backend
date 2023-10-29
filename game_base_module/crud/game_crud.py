from sqlalchemy.orm import Session

from game_base_module.models.game import Game
from game_base_module.schemas.game import GameCreate, GameUpdate


def get_game_by_id(db: Session, id: str):
    """
    Get game by id

    Parameters:
    - **id**: Game id
    """
    return db.query(Game).filter(Game.id == id).first()


def get_game_by_game_id_list(db: Session, game_id_list: list):
    """
    Get game by game id list

    Parameters:
    - **game_id_list**: List of game ids
    """
    return db.query(Game).filter(Game.id.in_(game_id_list)).all()


def get_game_by_name(db: Session, name: str):
    """
    Get game by name

    Parameters:
    - **name**: Game name
    """
    return db.query(Game).filter(Game.name == name).first()


def get_game_list(db: Session, offset: int = 0, limit: int = 100):
    """
    Get game list

    Parameters:
    - **offset**: Skip the first N games
    - **limit**: Limit the number of games returned
    """
    return db.query(Game).offset(offset).limit(limit).all()


def get_game_list_with_search_parameters(db: Session, offset: int = 0, limit: int = 100, search: str = None):
    """
    Get game list with search parameters

    Parameters:
    - **offset**: Skip the first N games
    - **limit**: Limit the number of games returned
    - **search**: Search games by name
    """
    if search is not None:
        return db.query(Game).filter(Game.name.icontains(search)).offset(offset).limit(limit).all()
    else:
        return db.query(Game).offset(offset).limit(limit).all()


def add_game(db: Session, game: GameCreate):
    """
    Add a new game to the database

    Parameters:
    - **game**: Game data to be added
    """
    db_game = Game(
        **game.model_dump(exclude_unset=True, exclude={"genre_list"}))
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game.id


def update_game(db: Session, game: GameUpdate, id: int):
    """
    Update game by id

    Parameters:
    - **id**: Game id
    - **game**: Updated game data
    """
    db_game = get_game_by_id(db=db, id=id)
    updated_game = game.model_dump(exclude_unset=True)

    # Get the list of attributes of the Game model
    model_attributes = db_game.__table__.columns.keys()

    for key, value in updated_game.items():
        if key in model_attributes:
            setattr(db_game, key, value)

    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def delete_game(db: Session, id: int):
    """
    Delete game by id

    Parameters:
    - **id**: Game id
    """
    db_game = get_game_by_id(db=db, id=id)
    db.delete(db_game)
    db.commit()
    return db_game
