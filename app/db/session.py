import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5433/incident_ops")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()