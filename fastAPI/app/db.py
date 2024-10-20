from fastapi import FastAPI,Response,status,HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time


# connecting and working with database with psycopg2 (no ORM used like sqlalchemy)


app=FastAPI()


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


class Product(BaseModel):
    title:str
    price:int


@app.get("/")
def home():
    cursor.execute(""" SELECT * FROM product ORDER BY id ASC """)
    all_data=cursor.fetchall()
    return {"message": all_data}

@app.post("/create")
def create_product(p:Product):
    cursor.execute(""" INSERT INTO product (title,price) VALUES (%s,%s) RETURNING *""",(p.title,p.price))
    pro=cursor.fetchone()
    conn.commit()
    return {"data":pro}

@app.patch("/update/{id:int}")
def update_post(id,p:Product):
    cursor.execute(""" UPDATE product SET title=%s, price=%s WHERE id=%s RETURNING * """,
                   (p.title,p.price,str(id)))
    upd_pro=cursor.fetchone()
    conn.commit()
    return {"data":upd_pro}


@app.delete("/delete/{id:int}")
def delete_product(id):
    cursor.execute(""" DELETE FROM product WHERE id=%s RETURNING * """,(str(id)))
    del_pro=cursor.fetchone()
    if del_pro==None:
        return { "msg":f"{id} id not found in database"}

    conn.commit()
    return {"data":del_pro}


@app.get("/product/{id:int}")
def get_one(id):
    cursor.execute(""" SELECT * FROM product WHERE id=%s""",(str(id)))
    one=cursor.fetchone()
    return {"data":one}
