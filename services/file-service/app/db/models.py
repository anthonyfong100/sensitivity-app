from sqlalchemy import TIMESTAMP, Column, Integer, String, Table
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.sql import func

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
    last_updated_time = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )
