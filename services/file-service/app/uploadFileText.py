from typing import Type

from fastapi.datastructures import Any, UploadFile
from starlette.datastructures import UploadFile as StarletteUploadFile


def get_file_ext(filename: str) -> str:
    return filename.split(".")[-1]


class UploadFileText(UploadFile):

    # overwrite default validation using pydantic to only alow files with .txt extensions
    @classmethod
    def validate(cls: Type["UploadFileText"], v: Any) -> Any:
        if not isinstance(v, StarletteUploadFile):
            raise ValueError(f"Expected UploadFile, received: {type(v)}")
        if get_file_ext(v.filename) != "txt":
            raise ValueError("Only file extensions of type txt is allowed")
        return v
