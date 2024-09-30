import curses
from turtle import title
from typing import Optional
from fastapi import Body, Depends, FastAPI, HTTPException, Response, status
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost',
                                database='fastapi',
                                user='postgres',
                                password='hello999',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was Successful...")
        break

    except Exception as error:
        print("Connecting to Database Failed!")
        print("Error: ",error)
        time.sleep(2)



@app.get("/")
def root():
    return {"message":"Root Endpoint"}

@app.get("/posts")
def get_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data" : posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.CreatePost, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # 1st Method
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    # 2nd Method (using the dictionary)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # Doing RETURNING * thing
    return {"data" : new_post}

@app.get("/posts/{id}",status_code=status.HTTP_200_OK)
def get_post(id:int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with the id:'{id}' Not found",
        )
    return {"data" : post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
    # delete_post = cursor.fetchone()
    # conn.commit()

    post= db.query(models.Post).filter(models.Post == id)

    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with '{id}' does not exist...",)
    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, updated_post:schemas.CreatePost, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""",
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with '{id}' does not exist...")
    
    post_query.update(updated_post.modeldump(),synchronize_session=False)
    db.commit()
    return {"Updated Post": post_query.first()}