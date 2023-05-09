from sqlalchemy.orm import Session
from models import Manga
from schemas import MangaSchema


def get_manga(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Manga).offset(skip).limit(limit).all()


def get_manga_by_id(db: Session, manga_id: int):
    return db.query(Manga).filter(Manga.id == manga_id).first()


def create_manga(db: Session, manga: MangaSchema):
    _manga = Manga(
        title=manga.title,
        author=manga.author,
        genre=manga.genre,
        rank=manga.rank,
        rating=manga.rating,
        type=manga.type
    )
    db.add(_manga)
    db.commit()
    db.refresh(_manga)
    return _manga


def remove_manga(db: Session, manga_id: int):
    _manga = get_manga_by_id(db=db, manga_id=manga_id)
    db.delete(_manga)
    db.commit()


def update_manga(db: Session, manga_id: int, title: str, author: str, genre: str, rank: str, type: str, rating: float, img: str):
    _manga = get_manga_by_id(db=db, manga_id=manga_id)

    _manga.title = title
    _manga.author = author
    _manga.genre = genre
    _manga.rank = rank
    _manga.type = type
    _manga.rating = rating
    _manga.img = img

    db.commit()
    db.refresh(_manga)
    return _manga
