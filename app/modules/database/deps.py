"""Sessions"""
from typing import Generator
from .engine import SessionLocal


def get_db() -> Generator:
    """ Получение сессии базы данных"""
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        db_session.close()
