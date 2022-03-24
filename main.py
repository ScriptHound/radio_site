from fastapi import FastAPI
from ming.odm import mapper

from db_models import Post
from validation_models import Post as ValidPost
from db_creds import session

app = FastAPI()


def find_objects(session, model_class, query=None):
    founding_session = session.impl
    result = founding_session\
        .find(mapper(model_class).collection, query).all()
    return result


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/post/")
async def create_post(post: ValidPost):
    Post(title=post.title, text=post.text)
    session.flush()
    return post


@app.get("/post/")
async def get_posts():
    posts = find_objects(session, Post)
    posts = [{'text': post['text'], 'title': post['title']} for post in posts]
    print(posts)
    return posts
