from fastapi import APIRouter, UploadFile, BackgroundTasks, File
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, RequestChapters, ChaptersSchema
import crudchapter
import json
import re
from models import Chapters

router_upload = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def update_chapter(db: Session, chapter, subtitle, mangaid, pages):
    _chapt = Chapters(subtitle=subtitle, pages=pages,
                      chapter=chapter, mangaid=mangaid)
    db.add(_chapt)
    db.commit()
    db.refresh(_chapt)
    print(_chapt)
    return _chapt


def read_json(file, db):
    data = json.load(file)
    for key, value in data.items():
        chapter = float(key.replace('Black Clover, Chapter ', ""))
        subtitle = value['chapter_name']
        pages = ",".join(x['src'] for x in value['chapters'])
        update_chapter(db, chapter=chapter, subtitle=subtitle,
                       pages=pages, mangaid=1)

    print("Finished")


@router_upload.post("/update")
async def upload_chapter(background_tasks: BackgroundTasks, db: Session = Depends(get_db), file: UploadFile = File(...)):
    background_tasks.add_task(read_json, file.file, db)
    # read_json(file.file, db)
    return {"filename": "Successfully Send to process the chapters"}
