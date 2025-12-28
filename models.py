from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from datetime import date

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    create_date = Column(Date, default=date.today())

    def __repr__(self):
        """객체를 문자열로 표현할 때 사용"""
        return f"Post(id = {self.id}, title = {self.title}, content = {self.content}, create_date = {self.create_date})"

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    create_date = Column(Date, default=date.today())
    post = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))

    def __repr__(self):
        """객체를 문자열로 표현할 때 사용"""
        return f"Comment(id = {self.id}, content = {self.content}, create_date = {self.create_date}, post = {self.post})"

