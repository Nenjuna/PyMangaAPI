from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, RequestManga, MangaSchema
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Manga Routes


@router.post("/create")
async def create_manga(request: RequestManga, db: Session = Depends(get_db)):
    crud.create_manga(db, manga=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Manga created successfully").dict(exclude_none=True)


@router.get("/")
async def get_mangas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _mangas = crud.get_manga(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_mangas)


@router.patch("/update")
async def update_manga(request: RequestManga, db: Session = Depends(get_db)):
    _mangas = crud.update_manga(db, manga_id=request.parameter.id,
                                title=request.parameter.title, author=request.parameter.author, rank=request.parameter.rank, genre=request.parameter.genre, rating=request.parameter.rating, type=request.parameter.type, img=request.parameter.img)
    return Response(status="Ok", code="200", message="Success update data", result=_mangas)


@router.delete("/delete")
async def delete_manga(request: RequestManga,  db: Session = Depends(get_db)):
    crud.remove_manga(db, manga_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router.get('/{manga_id}')
async def get_manga(manga_id, db: Session = Depends(get_db)):
    _manga = crud.get_manga_by_id(db, manga_id=manga_id)
    return Response(status="Ok", code="200", message="Book fetched successfully", result=_manga).dict(exclude_none=True)
