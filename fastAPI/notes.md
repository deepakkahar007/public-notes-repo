# FastAPI Notes:

# Table Of Contents

1. [Development Server](#to-start-development-server-use)
2. [Path Operations](#path-operations)
3. [Request Body](#to-extract-request-body)
4. [Pydantic Models](#work-with-pydantic-models)
5. [Pydantic With Default ](#pydantic-model-default-and-optional-values)
6. [Python Packages](#packages-in-python)
7. [Postgresql with Psycopg2](#connection-to-postgresql-database-using-psycopg2)
8. [DB Reconnect Method](#database-reconnect-method)
9. [Postgresql with SQLAlchemy](#connecting-postgresql-database-with-sqlalchemy-orm)
10. [CRUD With SQLAlchemy](#crud-with-sqlalchemy)

## to start development server use :

```bash
uvicorn main:app --reload
```

in this command the "main" means the file name of the root file and the "app" means the fast api instance.

### path operations :

the path operations matter fastapi always matchs the first path then return response
it always matches the method first then url

## To extract request body :

```python
    from fastapi.params import Body

    @app.post("/user")
    def user(payload : dict =Body(...)):
    print(payload)
    return {"data":payload}
```

the Body functions extract all the data out of request body. payload is a variable which is a dict type and assigned value from Body function

## work with pydantic models :

the pydantic library comes with fastapi but you can use it on any application, it just basically tells what kind of data are accepted. and it automatically extract body data.

```python

from pydantic import BaseModel

class Post(BaseModel):
    title:str
    desc:str
    is_published:bool

@app.post("/user")
def user(new_post:Post):
    print(new_post)
    return {"data":new_post}

```

### pydantic model default and optional values:

to create any field with default value use

```python
published:bool=True
```

to create any optional field use

```python
from typing import Optional

class Post:
    rating:Optional[int]=None
```

when working with pydantic model it return string but we can change it using .model_dump()

```python

new_post.model_dump()
```

### Response, status codes:

by default fastapi return 200 code for every request. to change codes and message use.

```python
from fastapi import FastAPI,Response,status

@app.post("/user")
def user(new_post:Post,response:Response):
    response.status_code=status.HTTP_201_CREATED
    print(new_post.model_dump())
    return {"data":new_post}
```

but there is an in built HTTPException class ca be use to overcome this problem.

```python
from fastapi import FastAPI,Response,status,HTTPException

@app.get("/about/{id}")
def about(id:int):
    if id == 7:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id found with this id {id}")
    return {"details":f"{id} id found"}
```

### set default status code

to set default status code on a perticular request, like every time someone hit post request give 201 status.

```python
@app.post("/user",status_code=status.HTTP_201_CREATED)
def user(new_post:Post):
    print(new_post.model_dump())
    return {"data":new_post}
```

## packages in python :

packages are just folder in python with a file like **init**.py file that will make a folder a package.

for eg:- app/**init**.py and any file

the files can be accessed by using .app/filename.

uvicorn package.filename:fastapi instance --reload

```bash
uvicorn app.db:app --reload
```

# Connection to postgresql database using psycopg2

firstly make sure that postgresql server up and running and there is a database for working.

```python
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn=psycopg2.connect(host='localhost',database='fastapi',user='deepak',password='deepak',cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("database connected successfully")
except Exception as error:
    print("database connection failed")
    print("error : ",error)

```

but in this setup the database connectivity might fail but the rest of appliction run normally. so thereis no point to work with application with no database.

# database reconnect method:

in this method the application tries to reconnect in a perticular time .

```python
import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='deepak',password='deepak',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connected successfully")
        break
    except Exception as error:
        print("database connection failed")
        print("error : ",error)
        time.sleep(2)
```

## To fetch all record from table :

```python
@app.get("/")
def home():
    cursor.execute(""" SELECT * FROM product ORDER BY id ASC """)
    all_data=cursor.fetchall()
    return {"message": all_data}
```

# connecting postgresql database with sqlalchemy ORM:

firstly create 2 files :
db.py = handle connection string and connectivity
models.py = handle all the models

## defining SQLALCHEMY_URL :

sy : SQLALCHEMY_DATABASE_URL='postgresql://<username>:<password>@<ip_address/hostname>/<database name>'
eg: SQLALCHEMY_DATABASE_URL='postgresql://deepak:deepak@localhost/fastapi'

db.py file:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL='postgresql://deepak:deepak@localhost/fastapi'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

```

model.py file :

```python
from .db import Base
from sqlalchemy import Column,Integer,String

class Post(Base):
    __tablename__="post"

    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    price=Column(Integer,nullable=False)
```

main.py file :

```python
from . import model
from .db import engine,SessionLocal

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## creating a route to handle request with database:

```python
from fastapi import FastAPI,Depends
from . import model
from .db import engine,SessionLocal
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"data":"working"}

@app.post("/post")
def create_post(db:Session = Depends(get_db)):
    return {"status":"success"}
```

## server Default and timestamps (created_at):

use server_default instead of default to set default value in table.

note : everytime you change any models or schema delete the existing db and restart the server
this problem can be fix by using ambratic package in fastapi doc

models.py file

```python
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
```

# CRUD with sqlalchemy:

## to fetch all records

```python
@app.get("/all")
def get_all(db:Session = Depends(get_db)):
   all=db.query(model.Post).all()
   return {"data":all}
```

## Create Record

use pydantic model to validate the value coming from request body.

```python
from pydantic import BaseModel

class Post(BaseModel):  # pydantic model
    title:str
    price:int
    offer:bool

@app.post("/post")
def create_post(p:Post ,db:Session = Depends(get_db)):
    new_post=model.Post(title=p.title,price=p.price,offer=p.offer)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"status":new_post}
```

db.add() = this method will add record in DB but no changes will refelect until you call commit()
db.commit() = it will save the new record and commit all changes to DB.
db.refresh() = this will return the updated and new post.

## get single record by id :

```python
@app.get("/id/{id:int}")
def get_id(id,db:Session = Depends(get_db)):
    new_id=db.query(model.Post).filter(model.Post.id==id).first()
    return {"data":new_id}
```

## Delete Any record by id :

```python
from fastapi import FastAPI,Depends,HTTPException,Response,status

@app.delete("/delete/{id:int}")
def delete_post(id,db:Session = Depends(get_db)):

    del_post=db.query(model.Post).filter(model.Post.id==id)

    if del_post.first() == None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"'{id}' this id not found")

    del_post.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
```

## Update Record :

```python
@app.patch("/update/{id:int}")
def update_post(id,p:Post,db:Session = Depends(get_db)):

    upd_id=db.query(model.Post).filter(model.Post.id==id)
    post=upd_id.first()

    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"'{id}' this id not found")

    upd_id.update(p.model_dump(),synchronize_session=False)
    db.commit()
    return {"data":upd_id.first()}

```

# pydantic vs sqlalchemy model

## pydantic model :

the pydantic model accept the request response data through pydantic model, basically it represent how data should be sendto a backend.

## sqlalchemy model :

the sqlalchemy model is db model which represent the column or table of db. it perform all te db operations like CRUD.

## creating schema file to import pydantic model

you can create a schema file to have all the pydantic model so you don't cluuter the main file

schema.py

```python
from pydantic import BaseModel

class Post(BaseModel):
    title:str
    price:int
    offer:bool

# class inheritance
class createPost(Post):
    pass
```

now you can use the schema for pydantic model and the schema file uses the classes so you can use anything which apply to python classes like inheritance.

# Response Model

<p>the response model can be use to send back the custom response data, it can be use to restict how much data you can send to client.</p>

## create response model

go to schema.py file and create a response schema
schema.py file :

```python
class PostResponse(Post):
    pass
    class Config:
        from_attributes=True
```

**note** : the config is important other wise it throws error.

Now Add response model in function decorators.

main.py file

```python
@app.post("/post", response_model=schema.PostResponse)
def create_post(p:schema.createPost ,db:Session = Depends(get_db)):
    new_post=model.Post(title=p.title,price=p.price,offer=p.offer)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
```

**note** : but whenever you send the list of data like all record url, where the url send back the list use typing list

## to get all record using response model and list

```python
from typing import List

@app.get("/all",response_model=List[schema.PostResponse])
def get_all(db:Session = Depends(get_db)):
    all=db.query(model.Post).all()
    return all
```

# FastAPI router :

<p>the fastapi router is use to separate the logic and routing of main file to another file. to start wit router create router folder.</p>

| file |     path     |          desc           |
| :--: | :----------: | :---------------------: |
| post | /router/post | route about posts, CRUD |
| user | /router/user | route about user, auth  |

## fastApi router setup

```python
from fastapi import APIRouter

router= APIRouter(prefix="/user")

@router.post("/create", status_code=status.HTTP_201_CREATED,response_model=schema.res_user)
def user_create(u:schema.user,db:Session = Depends(get_db)):
    u.password=hash(u.password)
    new_user=model.User(**u.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

**note** : now to use to use the router invoke it in main.py file

```python
from .router import user,post

app.include_router(user.router)
```

**note** : now the prefix means that you don't have to manually add path to the api, just add specific path.

## password hashing using passlib[bcrypt]

to hash the password use passlib library with bcrypt algorithm. install library using :

```bash
pip install passlib[bcrypt]
```

after installing setup the hsahing logic on another file called utils.py

```python
from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash(password:str):
    return pwd_context.hash(password)
```

now in user.py file:

```python
from ..utils import hash

@router.post("/create", status_code=status.HTTP_201_CREATED,response_model=schema.res_user)
def user_create(u:schema.user,db:Session = Depends(get_db)):
    u.password=hash(u.password)
    new_user=model.User(**u.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```
