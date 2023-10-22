from sqlalchemy import Column, ForeignKey, Integer, String
from core.db.db_setup import Base


class BudMatchAssociation(Base):
    """
    Bud match association model

    Fields:
    - **match_id**: Match id
    - **user_id**: User id
    """
    __tablename__ = "bud_match_associations"

    match_id = Column(Integer, ForeignKey("bud_matches.id"), primary_key=True)
    user_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
