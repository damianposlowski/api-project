# to run live server type in the terminal:
# $ uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Dude!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']}; content: {payLoad['content']}"}