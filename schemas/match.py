from datetime import datetime
from pydantic import BaseModel


class MatchBase(BaseModel):
    player1: int
    player2: int


class MatchCreate(MatchBase):
    pass


class Match(MatchBase):
    match_id: int
    opponent: int
    winner: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True