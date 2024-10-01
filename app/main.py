from enum import auto
from typing import Optional, List
from fastapi import Body, Depends, FastAPI, HTTPException, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
# local imports
from app import models, schemas
from app.database import Base, engine, get_db
from app.routers import post,user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Connect to the db
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


app.include_router(post.router)
app.include_router(user.router)

# Root
@app.get("/")
def root():
    return {"message":"Root Endpoint"}