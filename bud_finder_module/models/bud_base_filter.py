from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

from core.db.db_setup import Base
from core.db.models.mixins import Timestamp
from core.constants import CountryEnum


class BudBaseFilter(Timestamp, Base):
    """
    BudFilter model

    Fields:
    - **user_id**: User uuid
    - **min_age_preference**: Minimum preferred age
    - **max_age_preference**: Maximum preferred age
    - **country_preference**: Preferred country
    """
    __tablename__ = "bud_base_filters"

    user_id = Column(String, ForeignKey("users.uuid"), primary_key=True)
    min_age_preference = Column(Integer, nullable=False)
    max_age_preference = Column(Integer, nullable=False)
    country_preference = Column(ENUM(CountryEnum), nullable=False)

    # Define the relationship to User model
    owner = relationship("User", back_populates="filters", uselist=False)

    # Define the relationship to BudGenderFilter model
    gender_filters = relationship(
        "BudGenderFilter", back_populates="base_filters")
