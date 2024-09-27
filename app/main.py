from typing import Optional
from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from random import randrange

app = FastAPI()

my_posts = [{
        "id" : 1,
        "title" : "First Post",
        "content" : "First day of learning to create APIs."
    },
    {
        "id" : 2,
        "title" : "Second Post",
        "content" : "Second day of learning to create APIs."
    }]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = 0

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

def find_post_index(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index

@app.get("/")
def root():
    return {"message":"Hello World! Usman."}

@app.get("/posts")
def get_post():
    return {"data" : my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,10000)
    my_posts.append(post_dict)
    return {"data" : post_dict}

@app.get("/posts/{id}",status_code=status.HTTP_200_OK)
def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post Not found",
        )
    return {"data" : post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with '{id}' does not exist...",)
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with '{id}' does not exist...")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"Updated Post": post}