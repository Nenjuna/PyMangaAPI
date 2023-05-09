from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, RequestChapters, ChaptersSchema
import crudchapter

router_chapters = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_chapters.post("/create")
async def create_chapter(request: RequestChapters, db: Session = Depends(get_db)):
    crudchapter.create_chapter(db, chapter=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Chapter created successfully").dict(exclude_none=True)


@router_chapters.get("/")
async def get_chapters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _chapters = crudchapter.get_chapters(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_chapters)


@router_chapters.patch("/update")
async def update_chapter(request: RequestChapters, db: Session = Depends(get_db)):
    _chapters = crudchapter.update_chapter(db, chapter_id=request.parameter.id,
                                           chapter=request.parameter.chapter, subtitle=request.parameter.subtitle, mangaid=request.parameter.mangaid, pages=request.parameter.pages)
    return Response(status="Ok", code="200", message="Success update data", result=_chapters)


# @router_chapters.delete("/delete")
# async def delete_manga(request: RequestChapters,  db: Session = Depends(get_db)):
#     crud.remove_manga(db, manga_id=request.parameter.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


# @router_chapters.get('/{manga_id}')
# async def get_manga(manga_id, db: Session = Depends(get_db)):
#     _manga = crud.get_manga_by_id(db, manga_id=manga_id)
#     return Response(status="Ok", code="200", message="Book fetched successfully", result=_manga).dict(exclude_none=True)
