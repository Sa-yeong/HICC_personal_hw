from fastapi import APIRouter, Body
from models import Post, Comment
import data as service

router = APIRouter(prefix='/posts')

@router.get("/")
def get_posts() -> list[Post]:
    return service.get_posts()

@router.get("/{id}")
def get_post(id: int) -> Post:
    return service.get_post(id)

@router.post("/")
def create(title:str=Body(..., embed=True), content: str=Body(..., embed=True)):
    return service.create_post(title, content)

@router.get("/{post_id}/comment")
def get_comments(post_id: int) -> list[Comment] | dict:
    return service.get_comments(post_id)

@router.post("/{post_id}/comment")
def create_comment(post_id: int, content: str=Body(..., embed=True)):
    return service.create_comment(post_id, content)

# @router.post("/{post_id}/comment")
# def create_comment(comment: Comment) -> Comment:
#     return c_service.create(comment)