from fastapi import APIRouter

from chat_module import endpoints as chat_router

ws_router = APIRouter()

ws_router.include_router(chat_router.router, prefix="", tags=["Chat"])
