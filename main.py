from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    name: str
    roll: str
    published: bool = True
    rating: Optional[int] = None
    

@app.get("/")
def root():
    return {"message": "Hello Dear"}

@app.get("/about")
def root():
    return {"Hi there"}

@app.post("/createposts")
def create_posts(post: Post):
    name = post.name
    roll = post.roll
    print(post)
    return {"data": post}