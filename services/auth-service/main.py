import os

import uvicorn
from app import (
    config,
)  # this line needs to be the first few as it imports the .env into sys variable
from app.db import database, models
from app.routes import auth_router
from dotenv import load_dotenv
from fastapi import FastAPI

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    docs_url="/api/auth/docs",
    openapi_url="/api/auth/openapi.json",
    redoc_url=None,
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
