from sqlalchemy.orm import Session
from models import Post, Comment
import schemas
from fastapi.responses import JSONResponse

# Post용

def get_posts(db: Session) -> list[Post]:
    """모든 게시물을 조회합니다."""
    return db.query(Post).all()

def get_post(db: Session, post_id : int) -> Post:
    """특정한 한 게시물을 조회합니다."""
    posts = db.query(Post).all()

    for _post in posts:
        if _post.id == post_id :
            return _post
    return JSONResponse(
        status_code=404,
        content={
            "status_code" : 404,
            "error" : "POST_NOT_FOUND",
            "message" : "존재하지 않는 게시글입니다."
        }
    )

def create_post(db: Session, post: schemas.PostCreate):
    """새로운 게시글을 작성합니다."""
    
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return {"message" : "성공적으로 등록됐습니다."}

# Comment 용

def get_comments(db: Session, post_id: int) -> list[Comment] | dict:
    """특정 게시물의 모든 댓글을 조회합니다."""
    posts = db.query(Post).all()
    comments = db.query(Comment).filter(Comment.post == post_id).all()

    post_ids = []
    for _post in posts:
        post_ids.append(_post.id)
    if post_id in post_ids:
        if len(comments)>0:
            return comments
        else:
            return {"message" : "존재하는 댓글이 없습니다."}
    else:
        return JSONResponse(
            status_code=404,
            content={
                "status_code" : 404,
                "error" : "POST_NOT_FOUND",
                "message" : "존재하지 않는 게시글입니다."
            }
        )

def create_comment(db: Session, comment: schemas.CommentCreate, post_id: int):
    posts = db.query(Post).all()

    post_ids=[]
    for _post in posts:
        post_ids.append(_post.id)
    
    if post_id in post_ids:
        """새로운 댓글을 생성합니다."""
        new_comment = Comment(**comment.model_dump(), post=post_id)
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)

        return {"message" : "성공적으로 등록됐습니다."}
    else:
        return JSONResponse(
            status_code=404,
            content={
                "status_code" : 404,
                "error" : "POST_NOT_FOUND",
                "message" : "존재하지 않는 게시글입니다."
            }
        )