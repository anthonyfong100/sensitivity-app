import os
import shutil

from fastapi import APIRouter, File, Response, UploadFile, status

from .uploadFileText import UploadFileText
from .utils import get_file_size

file_router = APIRouter()


@file_router.get("/")
async def root():
    return Response(status_code=status.HTTP_200_OK)


@file_router.post("/upload/")
async def create_upload_file(file: UploadFileText = File(...)):
    upload_folder = os.getenv("FILE_UPLOAD_DIR")
    file_object = file.file
    # create empty file to copy the file_object to
    upload_folder_path = os.path.join(upload_folder, file.filename)
    upload_folder = open(upload_folder_path, "wb+")
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    return {
        "filename": file.filename,
        "file size": get_file_size(upload_folder_path),
        "file path": upload_folder_path,
    }
