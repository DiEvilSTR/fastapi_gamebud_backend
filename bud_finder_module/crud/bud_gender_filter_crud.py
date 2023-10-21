from sqlalchemy.orm import Session
from typing import List

from bud_finder_module.models.bud_gender_filter import BudGenderFilter
from core.constants import GenderEnum


# Not using this function
def get_filter_by_user_id(db: Session, user_id: str):
    """
    Get filter by user id

    Parameters:
    - **user_id**: User id
    """
    return db.query(BudGenderFilter).filter(BudGenderFilter.user_id == user_id).first()


def add_filter(db: Session, user_id: str, gender_preference_list: List[GenderEnum]):
    """
    Add a new filter to the database

    Parameters:
    - **user_id**: User id
    - **gender_preference_list**: Gender preference list
    """
    db_gender_preference_list = []
    for gender_preference in gender_preference_list:
        db_gender_preference = BudGenderFilter(
            user_id=user_id, gender_preference=gender_preference)
        db_gender_preference_list.append(db_gender_preference)
    db.bulk_save_objects(db_gender_preference_list)
    db.commit()


def delete_filter(db: Session, user_id: str, gender_preference: str = None):
    """
    Delete filter by user id

    Parameters:
    - **user_id**: User id
    """
    filter_conditions = [BudGenderFilter.user_id == user_id]

    if gender_preference is not None:
        filter_conditions.append(
            BudGenderFilter.gender_preference == gender_preference)

    db.query(BudGenderFilter).filter(
        *filter_conditions).delete(synchronize_session=False)
    db.commit()


def update_filter(db: Session, user_id: str, updated_preference_list: List[GenderEnum]):
    """
    Update filter by user id

    Parameters:
    - **user_id**: User id
    - **updated_preference_list**: List of gender preferences
    """
    db_gender_preferences = db.query(BudGenderFilter).filter(
        BudGenderFilter.user_id == user_id).all()
    current_gender_preferences = [
        preference.gender_preference for preference in db_gender_preferences]
    updated_preferences = updated_preference_list

    # Delete all current preferences that are not in the updated list
    for preference in current_gender_preferences:
        if preference not in updated_preferences:
            delete_filter(db=db, user_id=user_id, gender_preference=preference)

    # Add all updated preferences that are not in the current list
    for preference in updated_preferences:
        if preference not in current_gender_preferences:
            add_filter(db=db, user_id=user_id,
                       gender_preference_list=[preference])
