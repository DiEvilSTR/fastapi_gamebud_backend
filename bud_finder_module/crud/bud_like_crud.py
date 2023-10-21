from sqlalchemy.orm import Session

from bud_finder_module.models.bud_like import BudLike
from bud_finder_module.schemas.bud_like import BudLikeCreate


def check_like_mutuality(db: Session, swiper_id: str, swiped_id: str):
    """
    Check mutual like and return True if it exists

    Parameters:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    """
    db_like = db.query(BudLike).filter(
        BudLike.swiper_id == swiped_id,
        BudLike.swiped_id == swiper_id,
        BudLike.is_like == True
    ).first()

    if db_like is not None:
        return True
    else:
        return False


def like_bud(db: Session, swiper_id: str, swiped_id: str):
    """
    Create a new like in the database

    Parameters:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    """
    db_like = BudLike(swiper_id=swiper_id,
                      swiped_id=swiped_id,
                      is_like=True)
    db.add(db_like)
    db.commit()


def dislike_bud(db: Session, swiper_id: str, swiped_id: str):
    """
    Create a new dislike in the database

    Parameters:
    - **swiper_id**: Swiper id
    - **swiped_id**: Swiped id
    """
    # Create dislike
    db_dislike = BudLike(swiper_id=swiper_id,
                         swiped_id=swiped_id,
                         is_like=False)
    db.add(db_dislike)
    db.commit()


def get_likes_by_swiper_id(db: Session, swiper_id: str):
    """
    Get likes from buds by swiper id

    Parameters:
    - **swiper_id**: Swiper id
    """
    return db.query(BudLike).filter(BudLike.swiped_id == swiper_id).all()


def get_number_of_likes_for_user(db: Session, user_id: str):
    """
    Get number of likes for user

    Parameters:
    - **swiper_id**: Swiper id
    """
    return db.query(BudLike).filter(
        BudLike.swiped_id == user_id,
        BudLike.is_like == True
    ).count()


def delete_likes_for_matched_users(db: Session, user_id: str, matched_user_id: str):
    """
    Delete likes for matched users

    Parameters:
    - **user_id**: User id
    - **matched_user_id**: Matched user id
    """
    db.query(BudLike).filter(
        BudLike.swiper_id == user_id,
        BudLike.swiped_id == matched_user_id
    ).delete()
    db.query(BudLike).filter(
        BudLike.swiper_id == matched_user_id,
        BudLike.swiped_id == user_id
    ).delete()
    db.commit()
