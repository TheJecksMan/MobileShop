"""Sessions"""
from .async_engine import async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncSession:
    async with async_session.begin() as session:
        yield session
