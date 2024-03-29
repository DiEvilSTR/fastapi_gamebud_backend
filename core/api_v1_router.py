from fastapi import APIRouter

from bud_finder_module import endpoints as bud_finder_router
from game_base_module import endpoints as games_router
from user_profile_module import endpoints as users_router

api_router = APIRouter()

api_router.include_router(users_router.router, prefix="/user", tags=["User"])
api_router.include_router(
    games_router.router, prefix="/game_base", tags=["Game base"])
api_router.include_router(
    bud_finder_router.router, prefix="/bud_finder", tags=["Bud finder"])
