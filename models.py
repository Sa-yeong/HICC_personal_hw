from pydantic import BaseModel, Field
from datetime import date

class Post(BaseModel):
    id : int
    title : str = Field(max_length=30, description="게시글 제목")
    content : str
    create_date : date = Field(default=date.today(), description="게시글 작성 날짜")

class Comment(BaseModel):
    id : int
    content : str = Field(max_length=200, description="댓글 내용")
    create_date : date = Field(default=date.today(), description="댓글 작성 날짜")
    post : int
