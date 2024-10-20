from pydantic import BaseModel

class Post(BaseModel):
    title:str
    price:int
    offer:bool

# class inheritance
class createPost(Post):
    pass

class PostResponse(Post):
    pass
    class Config:
        from_attributes=True
