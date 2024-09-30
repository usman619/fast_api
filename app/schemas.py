from pydantic import BaseModel

# Structure of the Request
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    pass