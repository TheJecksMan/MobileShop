"""FastApi"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from api.v1.api import api_router
from core.setting import TITLE, DESCRIPTION, VERSION, DEV_MODE


if DEV_MODE:
    app = FastAPI()
else:
    app = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION,
        openapi_url=None
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['GET', 'POST'],
)
app.add_middleware(GZipMiddleware, minimum_size=800)

app.include_router(api_router, prefix='/api')
