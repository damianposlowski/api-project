# to run live server type in the terminal:
# $ uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "fun title for my post", "content": "engaging content of this post", "id": 2}
    ]

def find_post(id):
    for post in my_posts:
        if post["id"] == int(id):
            return post


@app.get("/")
def root():
    return {"message": "Hello Dude!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = list(filter(lambda item: item["id"] == int(id), my_posts))[0]
    return {"post detail": post}
    # return find_post(id)