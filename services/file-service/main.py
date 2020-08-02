import os

import uvicorn
from app import (
    config,
)  # this line needs to be the first few as it imports the .env into sys variable
from app.routes import file_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(file_router, prefix="/api/file", tags=["file"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
