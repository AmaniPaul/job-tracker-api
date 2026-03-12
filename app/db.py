from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./jobtracker.db"

engine = create_engine (
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass

def get_db():
    """
    FastAPI dependency that provides a database session per request.
    Ensures the session closes even if an error occurs.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()