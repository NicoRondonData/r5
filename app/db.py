import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_HOST = os.environ.get(
    "DATABASE_HOST", "postgresql+asyncpg://localhost@r5-db:5432/r5"
)
engine = create_async_engine(DATABASE_HOST, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        return 0


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        yield session
