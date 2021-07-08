from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text

app = FastAPI()

model = []

# post model
class Post(BaseModel):
    id: int
    Titulo: str
    Autor: str
    Conteudo: Text

@app.get("/blog")
def get_posts():
    return model

@app.post("/blog")
def add_post(post: Post):
    model.append(post.dict())
    return model[-1]

#@app.get("/blog/{post_id}")
#def get_post(post_id: int):
#    post = post_id - 1
#    return postdb[post]

@app.post("/blog/{post_id}")
def update_post(post_id: int, post: Post):
    model[post_id] = post
    return {"message": "Post foi atualizado com sucesso!"}

@app.delete("/blog/{post_id}")
def delete_post(post_id: int):
    model.pop(post_id-1)
    return {"message": "Post foi deletado com sucesso!"}