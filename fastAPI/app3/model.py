from .db import Base
from sqlalchemy import Column, ForeignKey,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Relationship


class User(Base):
    __tablename__ = "user"
    
    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Post(Base):
    __tablename__ = "post1"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String)
    desc=Column(String)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    author=Column(Integer,ForeignKey("user.id",ondelete="CASCADE"),nullable=False)

    owner=Relationship("User")
