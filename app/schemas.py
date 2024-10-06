from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated
# from pydantic.types import conint
from datetime import datetime

# Structure of the Request
# USER
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]

# POST
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True # called orm_mode previously

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class Vote(BaseModel):
    post_id: int
    vote_dir: Annotated[int, Field(strict=True, ge=0, le=1)]