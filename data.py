from models import Post, Comment
from fastapi import HTTPException
from fastapi.responses import JSONResponse

# 가짜 데이터 만들기

_posts = [
    Post(
        id=1,
        title="안녕하세요",
        content="반가워요",
        create_date="2025-06-30"
    ),
    Post(
        id=2,
        title="안녕하세요",
        content="반가워요",
        create_date="2025-06-30"
    )
]

_comments = [
    Comment(
        id = 3,
        content="네, 반갑습니다",
        create_date= "2025-06-28",
        post=2
    ),
    Comment(
        id=4,
        content="정말로요",
        create_date="2024-06-30",
        post=2
    )
]

# Post용
# 가짜 데이터를 이용한 함수 만들기

def get_posts() -> list[Post]:
    return _posts

def get_post(post_id : int) -> Post:
    for _post in _posts:
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

def create_post(title: str, content: str):
    """게시글 작성하기"""
    post_id = 0
    for _post in _posts:
        if post_id < _post.id:
            post_id = _post.id
    
    new_post = Post(id = post_id+1, title=title, content=content)
    _posts.append(new_post)
    
    return {"message" : "성공적으로 등록됐습니다."}

# Comment 용
# 가짜 데이터를 활용한 함수 만들기

def get_comments(post_id: int) -> list[Comment] | dict:
    post_ids = []
    for _post in _posts:
        post_ids.append(_post.id)
    if post_id in post_ids:
        li = []

        for _comment in _comments:
            if _comment.post == post_id:
                li.append(_comment)
        if len(li) > 0 :
            return li
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

# def create_comment(post_id: int, content: str) -> Comment:
#     post_ids=[]
#     for _post in _posts:
#         post_ids.append(_post.id)

#     if post_id in post_ids:
#         comment_id = 0
#         for _comment in _comments:
#             if comment_id < _comment.id:
#                 comment_id = _comment.id
#         comment = Comment(id=comment_id+1, content=content, post=post_id)
#         return comment
#     else:
#         raise HTTPException(status_code=404, detail="존재하지 않는 게시글입니다.")

def create_comment(post_id: int, content: str):
    post_ids=[]
    for _post in _posts:
        post_ids.append(_post.id)
    
    if post_id in post_ids:
        """생성된 댓글 추가하기"""
        comment_id = 0
        for _comment in _comments:
            if comment_id < _comment.id:
                comment_id = _comment.id
        comment = Comment(id=comment_id+1, content=content, post=post_id)
        _comments.append(comment)

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