import uvicorn

from fastapi import FastAPI

from core.api_v1_router import api_router
from core.config import settings
from core.db.db_setup import engine

# Models
from bud_finder_module.models import bud_like, bud_match
from user_profile_module.models import user, user_game_association
from game_base_module.models import game, game_genre, game_genre_association

# Create all tables
bud_like.Base.metadata.create_all(bind=engine)
bud_match.Base.metadata.create_all(bind=engine)
game.Base.metadata.create_all(bind=engine)
game_genre.Base.metadata.create_all(bind=engine)
game_genre_association.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
user_game_association.Base.metadata.create_all(bind=engine)

# Application
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version="0.0.1",
    contact={
        "name": settings.AUTHOR,
        "email": settings.AUTHOR_EMAIL,
    }
)

app.include_router(api_router, prefix=settings.API_V1_STR)
