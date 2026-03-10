from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    id: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]
    

@app.get("/")
def root():
    return {"message": "Hello Dear"}

@app.get("/posts")
def root():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post.id= random.randint(0, 100000000)
    my_posts.append(post)
    return {"data": post}