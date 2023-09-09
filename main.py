import uvicorn

from fastapi import FastAPI

from core.api_v1_router import api_router
from core.config import settings
from core.db.db_setup import engine

# Models
from user_profile_module.models import user
from game_base_module.models import game, game_genre, association

# Create all tables
user.Base.metadata.create_all(bind=engine)
game.Base.metadata.create_all(bind=engine)
game_genre.Base.metadata.create_all(bind=engine)
association.Base.metadata.create_all(bind=engine)

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
