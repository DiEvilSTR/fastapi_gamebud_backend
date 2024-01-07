from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from core.config import settings

# Engine and SessionLocal
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    connect_args={},
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)

Base = declarative_base()


def get_db():
    """
    DB Session

    Returns:
    - **Session**: DB Session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
