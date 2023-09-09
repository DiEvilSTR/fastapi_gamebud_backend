from fastapi import APIRouter

from user_profile_module import endpoints as users_router
from game_base_module import endpoints as games_router

api_router = APIRouter()

api_router.include_router(users_router.router, prefix="/user", tags=["user"])
api_router.include_router(
    games_router.router, prefix="/game_base", tags=["game base"])
