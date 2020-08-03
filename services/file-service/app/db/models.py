from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.schema import UniqueConstraint

from .database import Base


class File(Base):
    __tablename__ = "files"
    __table_args__ = (
        UniqueConstraint("username", "filename", name="_username_filename_uc"),
    )
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    filename = Column(String, index=True)
    filesize = Column(Integer)
    filepath = Column(String)
