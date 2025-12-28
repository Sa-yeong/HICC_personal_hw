from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
import schemas, database
import crud as service

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix='/posts')

@router.get("/")
def get_posts(db: Session=Depends(get_db)) -> list[schemas.PostResponse]:
    return service.get_posts(db)

@router.get("/{id}")
def get_post(id: int, db: Session=Depends(get_db)) -> schemas.PostResponse:
    return service.get_post(db, id)

@router.post("/")
def create(post: schemas.PostCreate, db: Session=Depends(get_db)):
    return service.create_post(db, post)

@router.get("/{post_id}/comment")
def get_comments(post_id: int, db:Session=Depends(get_db)) -> list[schemas.CommentResponse] | dict:
    return service.get_comments(db, post_id)

@router.post("/{post_id}/comment")
def create_comment(post_id: int, comment: schemas.CommentCreate, db: Session=Depends(get_db)):
    return service.create_comment(db, comment, post_id)