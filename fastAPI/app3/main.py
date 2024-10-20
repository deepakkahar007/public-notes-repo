from fastapi import FastAPI
from . import model
from .db import engine
from .router import user,post,auth

model.Base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(user.router) 
app.include_router(post.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"msg":f"home route"}

# activate env
# source /home/deepak/Documents/fastAPI/env/bin/activate
