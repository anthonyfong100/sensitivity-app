from sqlalchemy import Column, Integer, String, Table

from .database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    filename = Column(String, index=True)
    filesize = Column(Integer)
    filepath = Column(String)
