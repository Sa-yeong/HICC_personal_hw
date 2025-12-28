from pydantic import BaseModel, Field
from datetime import date

# Post  Schema
class PostBase(BaseModel):
    title : str = Field(max_length=30)
    content : str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    create_date : date

    class Config: # ORM 모델을 Pydantic 모델로 자동 변환
        from_attributes = True

# Comment Schema
class CommentBase(BaseModel):
    content : str = Field(max_length=200)

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id : int
    create_date: date
    post: int

    class Config:
        orm_mode=True