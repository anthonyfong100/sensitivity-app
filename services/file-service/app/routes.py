from fastapi import APIRouter, Response, status

file_router = APIRouter()


@file_router.get("/")
async def root():
    return Response(status_code=status.HTTP_200_OK)
