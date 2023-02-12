"""Main module for launching the application"""
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from api.v1.api import api_router
from core.setting import TITLE, DESCRIPTION, VERSION

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    version=VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['GET', 'POST'],
)
app.add_middleware(GZipMiddleware, minimum_size=800)

app.include_router(api_router, prefix='/api')


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """Organization favicon.ico"""
    return FileResponse("static/favicon.ico")
