from pydantic import BaseModel


class FileUploadDetails(BaseModel):
    filename: str
    filesize: int
    filepath: str
