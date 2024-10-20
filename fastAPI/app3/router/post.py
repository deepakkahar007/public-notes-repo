from operator import contains
from fastapi import Depends,HTTPException,status,APIRouter,Response
from sqlalchemy.orm import Session
from .. import schema,db,model
from typing import List,Optional

from .. import oauth2 

router=APIRouter(prefix="/post",tags=["post"])

@router.post("/create")
def create_post(body:schema.post,
                db:Session=Depends(db.get_db),
                user_id:int=Depends(oauth2.get_current_user)):

    new_post= model.Post(author=user_id.id,**body.model_dump()) #type: ignore

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/all")
def get_all_post(db:Session=Depends(db.get_db)):
    
    all = db.query(model.Post).all()
    return all

@router.delete("/delete/{id:int}")
def delete_post(id,
                db:Session=Depends(db.get_db),
                user_id:int=Depends(oauth2.get_current_user)):
    
    del_post=db.query(model.Post).filter(model.Post.id==id)

    if del_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"no post found with {id} this id")
    
    if del_post.first().author != user_id.id:   #type:ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"not authorised to delete {id} this post")
    
    del_post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/getAllById",response_model=List[schema.res_post])
def get_all_by_id(db:Session=Depends(db.get_db),
                user_id:int=Depends(oauth2.get_current_user),
                search:Optional[str]="",
                limit:int=10):
    
    get_by_id=db.query(model.Post).filter(model.Post.author==user_id.id).limit(limit).all()  #type:ignore
    query=db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).all()

    return get_by_id
