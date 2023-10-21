from decouple import config
from sqlalchemy.orm import Session

from game_base_module.models.game_genre import GameGenre
from game_base_module.schemas.game_genre import GameGenreCreate, GameGenreUpdate


def get_game_genre_by_id(db: Session, id: str):
    """
    Get game genre by id

    Parameters:
    - **id**: Game genre id
    """
    db_game_genre = db.query(GameGenre).filter(GameGenre.id == id).first()

    if db_game_genre is None:
        return None

    # Calculate the number of associated games for game genre
    db_game_genre.number_of_games = db_game_genre.game_count or 0
    return db_game_genre


def get_game_genre_by_name(db: Session, name: str):
    """
    Get game genre by name

    Parameters:
    - **name**: Game genre name
    """
    db_game_genre = db.query(GameGenre).filter(GameGenre.name == name).first()

    if db_game_genre is None:
        return None

    # Calculate the number of associated games for game genre
    db_game_genre.number_of_games = db_game_genre.game_count or 0
    return db_game_genre


def get_game_genre_list(db: Session, offset: int = 0, limit: int = 100):
    """
    Get game genre list

    Parameters:
    - **offset**: Skip the first N game genres
    - **limit**: Limit the number of game genres returned
    """
    db_game_genres = db.query(GameGenre).offset(offset).limit(limit).all()

    # Calculate the number of associated games for each game genre
    for game_genre in db_game_genres:
        game_genre.number_of_games = game_genre.game_count or 0
    return db_game_genres


def add_game_genre(db: Session, game_genre: GameGenreCreate):
    """
    Add a new game genre to the database

    Parameters:
    - **game_genre**: Game genre data to be added
    """
    db_game_genre = GameGenre(**game_genre.model_dump(exclude_unset=True))
    db.add(db_game_genre)
    db.commit()
    db.refresh(db_game_genre)

    # Calculate the number of associated games for game genre
    db_game_genre.number_of_games = db_game_genre.game_count or 0
    return db_game_genre


def update_game_genre(db: Session, game_genre: GameGenreUpdate, id: int):
    """
    Update game genre by id

    Parameters:
    - **id**: Game genre id
    - **game_genre**: Updated game genre data
    """
    db_game_genre = get_game_genre_by_id(db=db, id=id)
    updated_game_genre = game_genre.model_dump(exclude_unset=True)
    for key, value in updated_game_genre.items():
        setattr(db_game_genre, key, value)
    db.add(db_game_genre)
    db.commit()
    db.refresh(db_game_genre)

    # Calculate the number of associated games for game genre
    db_game_genre.number_of_games = db_game_genre.game_count or 0
    return db_game_genre


def delete_game_genre(db: Session, id: int):
    """
    Delete game genre by id

    Parameters:
    - **id**: Game genre id
    """
    db_game_genre = get_game_genre_by_id(db=db, id=id)
    db.delete(db_game_genre)
    db.commit()
    return db_game_genre
