from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgrespass@db:5432/faraday"

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://docker_faraday_project:123456@db:5432/faraday"
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://docker_faraday_project:123456@db:5432/faraday"    

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()