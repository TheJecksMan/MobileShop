"""SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.setting import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=1800)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
