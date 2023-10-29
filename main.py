import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from core.api_v1_router import api_router
from core.config import settings
from core.db.db_setup import engine
from core.ws_router import ws_router


# Models
from bud_finder_module.models import bud_like, bud_match, bud_base_filter, bud_gender_filter
from chat_module.models import chat_message
from user_profile_module.models import user, user_game_association
from game_base_module.models import game, game_genre, game_genre_association


# Create all tables
bud_base_filter.Base.metadata.create_all(bind=engine)
bud_gender_filter.Base.metadata.create_all(bind=engine)
bud_like.Base.metadata.create_all(bind=engine)
bud_match.Base.metadata.create_all(bind=engine)
chat_message.Base.metadata.create_all(bind=engine)
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


@app.get("/")
async def redirect_to_docs():
    """
    Redirect to docs page
    """
    return RedirectResponse(url="/docs")


# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR) # Include API router
app.include_router(ws_router, prefix=settings.WS_V1_STR) # Include WebSocket router
