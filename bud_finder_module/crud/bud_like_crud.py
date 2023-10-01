from sqlalchemy.orm import Session

from bud_finder_module.models.bud_like import BudLike
from bud_finder_module.schemas.bud_like import BudLikeCreate, BudDislikeCreate


def check_like_mutuality(db: Session, like: BudLikeCreate):
    """
    Check mutual like and return True if it exists

    Parameters:
    - **like**: Like data to be added
    """
    db_like = db.query(BudLike).filter(
        BudLike.swiper_id == like.swiped_id,
        BudLike.swiped_id == like.swiper_id,
        BudLike.is_like == True
    ).first()

    if db_like is not None:
        return True


def like_bud(db: Session, like: BudLikeCreate):
    """
    Create a new like in the database

    Parameters:
    - **like**: Like data to be added
    """
    db_like = BudLike(swiper_id=like.swiper_id,
                      swiped_id=like.swiped_id,
                      is_like=True)
    db.add(db_like)
    db.commit()


def dislike_bud(db: Session, dislike: BudDislikeCreate):
    """
    Create a new dislike in the database

    Parameters:
    - **dislike**: Dislike data to be added
    """

    # Check if user already have like from this bud
    db_like = db.query(BudLike).filter(
        BudLike.swiper_id == dislike.swiped_id,
        BudLike.swiped_id == dislike.swiper_id,
        BudLike.is_like == True
    ).first()

    # If like exists, delete it
    if db_like is not None:
        db.delete(db_like)
        db.commit()

    # Create dislike
    db_dislike = BudLike(swiper_id=dislike.swiper_id,
                         swiped_id=dislike.swiped_id,
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
