from datetime import datetime
from pydantic import BaseModel


class MatchHistoryBase(BaseModel):
    opponent: int
    winner: int


class MatchHistoryCreate(MatchHistoryBase):
    pass


class MatchHistory(MatchHistoryBase):
    match_id: int
    opponent: int
    winner: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True