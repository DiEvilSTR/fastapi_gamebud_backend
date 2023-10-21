from sqlalchemy.orm import Session

from bud_finder_module.models.bud_base_filter import BudBaseFilter
from bud_finder_module.schemas.bud_filter import BudFilterCreate, BudFilterUpdate


def get_filter_by_user_id(db: Session, user_id: str):
    """
    Get filter by user id

    Parameters:
    - **user_id**: User id
    """
    return db.query(BudBaseFilter).filter(BudBaseFilter.user_id == user_id).first()


def add_filter(db: Session, user_id: str, filter: BudFilterCreate):
    """
    Add a new filter to the database

    Parameters:
    - **filter**: Filter data to be added
    """
    db_user_base_filter = BudBaseFilter(
        user_id=user_id,
        min_age_preference=filter.min_age_preference,
        max_age_preference=filter.max_age_preference,
        country_preference=filter.country_preference)
    db.add(db_user_base_filter)
    db.commit()


def update_filter(db: Session, user_id: str, filter: BudFilterUpdate):
    """
    Update filter

    Parameters:
    - **filter**: Filter data to be updated
    """
    db_user_base_filter = get_filter_by_user_id(db=db, user_id=user_id)
    updated_data = filter.model_dump(exclude_unset=True)

    # Get the list of attributes of the Game model
    model_attributes = db_user_base_filter.__table__.columns.keys()

    for key, value in updated_data.items():
        if key in model_attributes:
            setattr(db_user_base_filter, key, value)

    db.commit()


def delete_filter(db: Session, user_id: str):
    """
    Delete filter by user id

    Parameters:
    - **user_id**: User id
    """
    db_user_base_filter = get_filter_by_user_id(db=db, user_id=user_id)
    db.delete(db_user_base_filter)
    db.commit()
