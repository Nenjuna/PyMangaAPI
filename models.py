from sqlalchemy import Column, Integer, String, Float, ForeignKey
from config import Base
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


# class Book(Base):
#     __tablename__ = "book"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)


class Manga(Base):
    __tablename__ = "manga"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    rating = Column(Float)
    rank = Column(String)
    genre = Column(String)
    type = Column(String)
    img = Column(String)
    # chapters: Mapped[List['Chapters']] = relationship()


class Chapters(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    subtitle = Column(String)
    mangaid = Column(Integer, ForeignKey(
        'manga.id', ondelete="CASCADE"), nullable=False)
    pages = Column(String)
    chapter = Column(String)
