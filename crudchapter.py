from sqlalchemy.orm import Session
from models import Chapters
from schemas import ChaptersSchema


def get_chapters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Chapters).offset(skip).limit(limit).all()


def get_chapter_by_id(db: Session, chapter_id: int):
    return db.query(Chapters).filter(Chapters.id == chapter_id).first()


def create_chapter(db: Session, chapter: ChaptersSchema):
    _chapter = Chapters(subtitle=chapter.subtitle,
                        chapter=chapter.chapter, mangaid=chapter.mangaid, pages=chapter.pages)
    db.add(_chapter)
    db.commit()
    db.refresh(_chapter)
    return _chapter


def update_chapter(db: Session, chapter_id: int, subtitle: str, chapter: float, mangaid: int, pages: str):
    _chapter = get_chapter_by_id(db=db, chapter_id=chapter_id)
    _chapter.subtitle = subtitle
    _chapter.chapter = chapter
    _chapter.mangaid = mangaid
    _chapter.pages = pages

    db.commit()
    db.refresh(_chapter)
    return _chapter
