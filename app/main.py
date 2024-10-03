from fastapi import FastAPI
# local imports
from app import models
from app.database import engine
from app.routers import post,user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI() 


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# Root
@app.get("/")
def root():
    return {"message":"Root Endpoint"}