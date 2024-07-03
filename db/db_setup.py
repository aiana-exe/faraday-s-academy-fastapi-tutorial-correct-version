from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgrespass@localhost:5432/faraday"

# async
# SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgrespass@localhost:5432/faraday"    

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

# async
# engine = create_async_engine(
#     SQLALCHEMY_DATABASE_URL, echo=True,
# )
# SessionLocal = sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False,

#     autocommit=False, autoflush=False, future=True
# )

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# async
# async def get_db():
#     async with SessionLocal() as session:
#         yield session