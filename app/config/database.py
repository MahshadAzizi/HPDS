from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config.settings import settings

# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-engine
engine = create_engine(
    settings.DATABASE_URL, connect_args=settings.DATABASE_CONNECT_DICT
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    """
    Returns a new session for the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
