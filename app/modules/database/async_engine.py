"""database initialization"""
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from core.setting import SQLALCHEMY_ASYNC_DATABASE_URL


async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL, pool_recycle=1800, pool_pre_ping=True)
async_session = async_sessionmaker(
    async_engine, expire_on_commit=False
)
