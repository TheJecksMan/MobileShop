from fastapi import FastAPI
from core.setting import TITLE, DESCRIPTION, VERSION, CORS_POLICY

from api.v1.api import api_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    version=VERSION,
    license_info={
        "name": "MIT",
        "url": "http://exapmle.com",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_POLICY,
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api')
