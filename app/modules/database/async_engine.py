from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession
from core.setting import SQLALCHEMY_ASYNC_DATABASE_URL


async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL, pool_recycle=1800, pool_pre_ping=True)
async_session = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)
