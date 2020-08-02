import os


def get_file_size(filepath: str) -> str:
    b = os.path.getsize(filepath)  # result in bytes
    return b
