from pydantic import BaseModel, EmailStr
from typing import Optional

class user(BaseModel):
    id:int
    name:str
    email:EmailStr
    password:str

    class Config:
        from_attributes=True

class post(BaseModel):
    title:str
    desc:str
    
    class Config:
        from_attributes=True

class res_user(user):
    pass

class auth(BaseModel):
    email:str
    password:str

class res_auth(BaseModel):
    name:str
    email:EmailStr
    token:str

    class Config:
        from_attributes=True

class Token(BaseModel):
    jwt_token:str
    token_type:str


class Token_res(BaseModel):
    id:Optional[int] = None

class res_post(BaseModel):
    id:int
    title:str
    desc:str
    author:int
    owner:res_user

    class Config:
        from_attributes=True
