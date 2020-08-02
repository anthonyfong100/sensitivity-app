import os
import shutil

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, File, Response, UploadFile, status

from .db.crud import create_file
from .db.database import get_db
from .middleware import verify_token
from .schema import FileUploadDetails
from .uploadFileText import UploadFileText
from .utils import get_file_size, save_file_to_path

file_router = APIRouter()


@file_router.get("/")
async def root():
    return Response(status_code=status.HTTP_200_OK)


@file_router.post(
    "/upload/", response_model=FileUploadDetails, status_code=201
)
async def create_upload_file(
    file: UploadFileText = File(...),
    db: Session = Depends(get_db),
    username: str = Depends(verify_token),
):
    # save to local storage
    upload_folder = os.getenv("FILE_UPLOAD_DIR")
    file_object = file.file
    upload_folder_path = os.path.join(upload_folder, file.filename)
    save_file_to_path(file_object, upload_folder_path)

    # save to db
    file_size = get_file_size(upload_folder_path)
    create_file(
        db,
        username=username,
        filename=file.filename,
        filesize=file_size,
        filepath=upload_folder_path,
    )
    return {
        "filename": file.filename,
        "filesize": file_size,
        "filepath": upload_folder_path,
    }
