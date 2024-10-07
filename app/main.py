from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# local imports
from app import models
from app.database import engine
from app.routers import post,user, auth, vote

# models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

# origins that are allowed to making request to your api (usually you add your web app domain for security)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Disable methods like POST and DELETE
    allow_headers=["*"]
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Root
@app.get("/")
def root():
    return {"message":"Root Endpoint"}