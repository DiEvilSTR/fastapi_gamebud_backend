from fastapi import APIRouter

from user_profile_module import router as users_router

api_router = APIRouter()

api_router.include_router(users_router.router, prefix="/users", tags=["users"])