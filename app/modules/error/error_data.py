"""FastApi"""
from fastapi import HTTPException


def raise_error(error_code: int, detail: str = "error") -> None:
    """Вывод получаемого кода ошибки в запрос
    """
    raise HTTPException(
        status_code=error_code,
        detail=detail,
    )
