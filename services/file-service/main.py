import os

import uvicorn
from app import config
from app.db import database, models
from app.middleware import verify_token
from app.routes import file_router
from fastapi import Depends, FastAPI

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    docs_url="/api/file/docs",
    openapi_url="/api/file/openapi.json",
    redoc_url=None,
)

app.include_router(
    file_router,
    prefix="/api/file",
    tags=["file"],
    dependencies=[Depends(verify_token)],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
