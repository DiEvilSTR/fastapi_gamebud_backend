from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db import db_setup
from core.config import settings
from fixtures import data_for_db, generate_game_genre_base


# Create a database connection
db_url = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_for_populating = SessionLocal()

generate_game_genre_base.populate_database(db=db_for_populating, users=data_for_db.users,
                  genres=data_for_db.genres, games=data_for_db.games)