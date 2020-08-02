import os
import shutil
from tempfile import SpooledTemporaryFile


def get_file_size(filepath: str) -> str:
    b = os.path.getsize(filepath)  # result in bytes
    return b


def save_file_to_path(file: SpooledTemporaryFile, upload_folder_path: str):
    # create empty file to copy the file_object to
    upload_folder = open(upload_folder_path, "wb+")
    shutil.copyfileobj(file, upload_folder)
    upload_folder.close()
