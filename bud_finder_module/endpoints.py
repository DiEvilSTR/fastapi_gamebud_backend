from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from core.db import db_setup
from core.jwt_authentication.jwt_bearer import jwt_scheme

from bud_finder_module.crud import bud_base_filter_crud, bud_gender_filter_crud, bud_list_crud, bud_like_crud, bud_match_crud, bud_match_association_crud
from bud_finder_module.schemas.bud_filter import BudFilter, BudFilterCreate, BudFilterUpdate
from bud_finder_module.schemas.bud_like import BudLikeCreate
from bud_finder_module.schemas.bud_match import BudMatch, BudMatchForMatchList

# Import schemas from other modules
from user_profile_module.schemas.user import UserAsBud
from user_profile_module.crud import user_crud

router = APIRouter()


@router.get("/bud_list", response_model=List[UserAsBud], status_code=status.HTTP_200_OK)
def fetch_bud_list(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get list of new users

    Parameters:
    - **user_id**: User id
    """
    return bud_list_crud.fetch_potential_matches(db=db, user_id=current_user_id)


@router.post("/swipe", status_code=status.HTTP_201_CREATED)
def swipe_bud(swipe: BudLikeCreate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Swipe bud

    Parameters:
    - **swipe**: Swipe data
    - **user_id**: User id
    """
    # Check if bud exists
    db_bud = user_crud.get_user_by_uuid(db=db, uuid=swipe.swiped_id)
    if db_bud is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bud not found"
        )

    if not swipe.is_like:
        # Create dislike record
        bud_like_crud.dislike_bud(
            db=db, swiper_id=current_user_id, swiped_id=swipe.swiped_id)
    else:
        # Create like record
        bud_like_crud.like_bud(
            db=db, swiper_id=current_user_id, swiped_id=swipe.swiped_id)

        # Check if like is mutual and create match if it is
        if bud_like_crud.check_like_mutuality(db=db, swiper_id=current_user_id, swiped_id=swipe.swiped_id):

            # Create match record
            db_match_id = bud_match_crud.create_match(db=db)

            # Create bud match associations
            bud_match_association_crud.create_bud_match_associations(
                db=db,
                user_id_1=current_user_id,
                user_id_2=swipe.swiped_id,
                match_id=db_match_id
            )

            # Delete like records
            bud_like_crud.delete_likes_for_matched_users(
                db=db, user_id=current_user_id, matched_user_id=swipe.swiped_id)

            return Response(status_code=status.HTTP_201_CREATED, content="Match created")

    return Response(status_code=status.HTTP_201_CREATED, content="Like created")


@router.post("/filter", response_model=BudFilter, status_code=status.HTTP_201_CREATED)
def set_filter(filter: BudFilterCreate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Set filter for bud list

    Parameters:
    - **filter**: Filter data
    - **user_id**: User id
    """
    # Add base filter record
    bud_base_filter_crud.add_filter(
        db=db,
        user_id=current_user_id,
        filter=filter
    )

    # Add gender filter record
    bud_gender_filter_crud.add_filter(
        db=db,
        user_id=current_user_id,
        gender_preference_list=filter.gender_preference
    )

    # Return filter
    db_filter = bud_base_filter_crud.get_filter_by_user_id(
        db=db, user_id=current_user_id)
    db_gender_preferences = [
        preference_record.gender_preference for preference_record in db_filter.gender_filters]
    db_filter.gender_preference = db_gender_preferences

    return db_filter


@router.get("/filter", response_model=BudFilter, status_code=status.HTTP_200_OK)
def get_users_filters(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get user's filters

    Parameters:
    - **user_id**: User id
    """
    db_filter = bud_base_filter_crud.get_filter_by_user_id(
        db=db, user_id=current_user_id)
    db_gender_preferences = [
        preference_record.gender_preference for preference_record in db_filter.gender_filters]
    db_filter.gender_preference = db_gender_preferences

    return db_filter


@router.patch("/filter", response_model=BudFilter, status_code=status.HTTP_200_OK)
def update_users_filters(updated_filters: BudFilterUpdate, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    # Update gender preferences if updated
    if updated_filters.gender_preference:
        bud_gender_filter_crud.update_filter(
            db=db, user_id=current_user_id, updated_preference_list=updated_filters.gender_preference)

    # Update base filter
    if updated_filters.min_age_preference or updated_filters.max_age_preference or updated_filters.country_preference:
        db_filter = bud_base_filter_crud.update_filter(
            db=db, user_id=current_user_id, filter=updated_filters)

    # Return updated filter
    db_filter = bud_base_filter_crud.get_filter_by_user_id(
        db=db, user_id=current_user_id)
    db_gender_preferences = [
        preference_record.gender_preference for preference_record in db_filter.gender_filters]
    db_filter.gender_preference = db_gender_preferences

    return db_filter


@router.get("/likes", response_model=List[UserAsBud], status_code=status.HTTP_200_OK)
def get_liked_buds(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get list of bud who liked current user

    Parameters:
    - **user_id**: User id
    """
    return bud_list_crud.fetch_list_of_likes_to_user(db=db, user_id=current_user_id)


@router.get("/likes/count", response_model=int, status_code=status.HTTP_200_OK)
def get_number_of_likes_to_user(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get number of likes to current user

    Parameters:
    - **user_id**: User id
    """
    return bud_like_crud.get_number_of_likes_for_user(db=db, user_id=current_user_id)


@router.get("/matches/list", response_model=List[BudMatchForMatchList], status_code=status.HTTP_200_OK)
def get_matches(db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Get list of matches

    Parameters:
    - **user_id**: User id
    """
    # Get list of matches ids
    dm_matches_ids = bud_match_association_crud.get_bud_matches_ids(
        db=db, user_id=current_user_id)

    # Get list of matches
    db_matches = bud_match_crud.fetch_matches_for_user(
        db=db, user_id=current_user_id, matches_ids_list=dm_matches_ids)

    return db_matches


# Delete the match
@router.delete("/matches/{match_id}", status_code=status.HTTP_200_OK)
def delete_match(match_id: int, db: Session = Depends(db_setup.get_db), current_user_id: str = Depends(jwt_scheme)):
    """
    Delete match

    Parameters:
    - **match_id**: Match id
    - **user_id**: User id
    """
    # Get match data
    db_match = bud_match_crud.get_match_by_match_id(db=db, match_id=match_id)

    # Check if user has permission to delete match
    if not None and db_match.buds[1]["uuid"] != current_user_id and db_match.buds[0]["uuid"] != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have permission to delete this match."
        )

    # Check if match exists
    if db_match is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Match not found"
        )

    # Delete match
    bud_match_crud.delete_matches_from_matches_ids_list(
        db=db, matches_ids_list=[match_id])

    return Response(status_code=status.HTTP_200_OK, content="Match deleted")
