from .db import Base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__="post"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    price=Column(Integer,nullable=False)
    offer=Column(Boolean,server_default='FALSE',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))





