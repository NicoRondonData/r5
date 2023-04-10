from fastapi import FastAPI

from app.db import get_session, init_db
from app.repositories import AuthorRepository
from app.repositories_registry import RepositoriesRegistry


class R5App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        repositories_registry = RepositoriesRegistry(author_repository=AuthorRepository)

        self.get_db_session = get_session
        self.repositories_registry = repositories_registry


app = R5App()


@app.on_event("startup")
async def on_startup():
    # Database
    await init_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
