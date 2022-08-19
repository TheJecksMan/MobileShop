from fastapi import FastAPI
from core.setting import TITLE, DESCRIPTION, VERSION

from api.v1.api import api_router


app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    version=VERSION,
    license_info={
        "name": "MIT",
        "url": "http://exapmle.com",
    }
)

app.include_router(api_router, prefix='/api')
