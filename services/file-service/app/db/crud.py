from typing import List

from sqlalchemy.orm import Session

from . import models


def create_file(
    db: Session, username: str, filename: str, filesize: int, filepath: str
) -> models.File:
    db_file = models.File(
        username=username,
        filename=filename,
        filesize=filesize,
        filepath=filepath,
        sensitivity_score=-1,
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


def read_files(db: Session, **kwargs) -> List[models.File]:
    if kwargs:
        return db.query(models.File).filter_by(**kwargs).all()
    return db.query(models.File).all()


def update_file_sensitivity(db: Session, selector: dict, value: any):
    db.query(models.File).filter_by(**selector).update(
        {"sensitivity_score": value}
    )
    db.commit()
