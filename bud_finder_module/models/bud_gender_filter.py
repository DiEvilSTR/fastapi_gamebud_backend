from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp
from core.constants import GenderEnum


class BudGenderFilter(Timestamp, Base):
    """
    BudFilter model

    Fields:
    - **user_id**: User uuid
    - **gender_preference**: Preferred gender

    Relationships:
    - **owner**: User owner (one-to-one)
    """
    __tablename__ = "bud_gender_filters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("bud_base_filters.user_id"))
    gender_preference = Column(ENUM(GenderEnum), nullable=False)

    # Define the relationship to BudBaseFilter model
    base_filters = relationship(
        "BudBaseFilter", back_populates="gender_filters", uselist=False)
