from fastapi import FastAPI

from db_models import Post
from validation_models import Post as ValidPost
from db_creds import session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/post/")
async def create_post(post: ValidPost):
    Post(title=post.title, text=post.text)
    session.flush()
    return post
