from typing import List

from pydantic import BaseModel


class FileUploadDetails(BaseModel):
    filename: str
    filesize: int
    filepath: str


class FileResponseDetails(FileUploadDetails):
    id: int
    username: str
