from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Post(BaseModel):
    title:str
    desc:str
    is_published:bool=True
    rating:Optional[int]=None
    
@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about/{id}")
def about(id:int):
    if id == 7:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id found with this id {id}")

    return {"details":f"{id} id found"}

@app.post("/user",status_code=status.HTTP_201_CREATED)
def user(new_post:Post):
    print(new_post.model_dump())
    return {"data":new_post}



