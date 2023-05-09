from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class MangaSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    rank: Optional[str] = None
    type: Optional[str] = None
    rating: Optional[float] = None
    img: Optional[str] = None

    class Config:
        orm_mode = True


class RequestManga(BaseModel):
    parameter: MangaSchema = Field(...)


class ChaptersSchema(BaseModel):
    id: Optional[int] = None
    chapter: Optional[str] = None
    subtitle: Optional[str] = None
    mangaid: Optional[int] = None
    pages: Optional[str] = None

    class Config:
        orm_mode = True


class RequestChapters(BaseModel):
    parameter: ChaptersSchema = Field(...)
