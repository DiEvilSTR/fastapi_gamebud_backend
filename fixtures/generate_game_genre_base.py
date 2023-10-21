from sqlalchemy.orm import Session

from bud_finder_module.crud import bud_base_filter_crud, bud_gender_filter_crud
from bud_finder_module.schemas.bud_base_filter import BudBaseFilterCreate
from game_base_module.crud import game_crud, game_genre_crud, game_genre_association_crud
from game_base_module.schemas.game import GameCreate
from game_base_module.schemas.game_genre import GameGenreCreate
from user_profile_module.schemas.user import UserCreate
from user_profile_module.crud import user_crud, user_game_association_crud


# Add items to database
def populate_database(db: Session, users, genres, games):
    # # Add genres
    for genre in genres:
        new_genre = GameGenreCreate(**genre)
        game_genre_crud.add_game_genre(db=db, game_genre=new_genre)

    # Add games
    for game in games:
        new_game = GameCreate(**game)
        new_game_id = game_crud.add_game(db=db, game=new_game)
        game_genre_association_crud.add_association(
            db=db, game_id=new_game_id, association_list=game["genre_list"])

    # Add users
    for user in users:
        new_user = UserCreate(**user)
        db_new_user = user_crud.create_user(db=db, user=new_user)
        new_user_id = db_new_user.uuid

        # Add user-game associations
        user_game_association_crud.add_user_game_association(
            db=db, user_id=new_user_id, games_list=user["games"])

        # Add bud base filters
        bud_base_filters = BudBaseFilterCreate(**user["base_filters"])
        bud_base_filter_crud.add_filter(
            db=db, user_id=new_user_id, filter=bud_base_filters)

        # Add bud gender filters
        bud_gender_filter_crud.add_filter(
            db=db, user_id=new_user_id, gender_preference_list=user["gender_filter"])
