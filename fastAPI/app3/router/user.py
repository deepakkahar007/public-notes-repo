from fastapi import APIRouter,Depends, HTTPException,Response,status
from .. import schema,model,db
from sqlalchemy.orm import Session
from typing import List
from ..utils import hash

router= APIRouter(prefix="/user")

@router.post("/create", status_code=status.HTTP_201_CREATED,response_model=schema.res_user)
def user_create(u:schema.user,db:Session = Depends(db.get_db)):
    u.password=hash(u.password)
    new_user=model.User(**u.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    
@router.get("/{id:int}",response_model=schema.res_user)
def get_id(id,db:Session = Depends(db.get_db)):
    new_id=db.query(model.User).filter(model.User.id==id).first()
    if new_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no id found with this {id} id")
    return new_id

@router.get("/all",response_model=List[schema.res_user])
def get_all(db:Session=Depends(db.get_db)):
    all=db.query(model.User).all()
    return all

@router.patch("/update/{id:int}")
def update_user(id):
    return id

@router.delete("/delete/{id:int}")
def delete_user(id,db:Session=Depends(db.get_db)):

    del_user=db.query(model.User).filter(model.User.id==id)

    if del_user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No user found with {id} id")
    
    del_user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

