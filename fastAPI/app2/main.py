from fastapi import FastAPI,Depends,HTTPException,Response,status
from . import model, schema
from .db import engine,get_db
from sqlalchemy.orm import Session
from typing import List

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.patch("/update/{id:int}")
def update_post(id,p:schema.Post,db:Session = Depends(get_db),response_model=schema.PostResponse):
    upd_id=db.query(model.Post).filter(model.Post.id==id)
    post=upd_id.first()
    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"'{id}' this id not found")
    upd_id.update(p.model_dump(),synchronize_session=False)
    db.commit()
    return upd_id.first()

@app.delete("/delete/{id:int}")
def delete_post(id,db:Session = Depends(get_db)):
    del_post=db.query(model.Post).filter(model.Post.id==id)
    if del_post.first() == None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"'{id}' this id not found")
    del_post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/id/{id:int}",response_model=schema.PostResponse)
def get_id(id,db:Session = Depends(get_db)):
    new_id=db.query(model.Post).filter(model.Post.id==id).first()
    if new_id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} this id not found")
    return new_id

@app.post("/post", response_model=schema.PostResponse)
def create_post(p:schema.createPost ,db:Session = Depends(get_db)):
    new_post=model.Post(title=p.title,price=p.price,offer=p.offer)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/all",response_model=List[schema.PostResponse])
def get_all(db:Session = Depends(get_db)):
    all=db.query(model.Post).all()
    return all




