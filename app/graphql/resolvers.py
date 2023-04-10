# resolvers.py
from typing import List

import strawberry
from fastapi import Depends
from sqlalchemy import select
from strawberry import Schema

from app.db import get_session
from app.graphql.types import AuthorType, InputAuthorType
from app.models import Author


@strawberry.type
class AuthorQuery:
    @strawberry.field
    async def all_authors(self) -> List[AuthorType]:
        async with get_session() as session:
            statement = select(Author)
            result = await session.execute(statement)
            records = result.scalars().all()
            return records


@strawberry.type
class AuthorMutation:
    @strawberry.mutation
    async def create_author(self, author: InputAuthorType) -> AuthorType:
        async with get_session() as session:
            author = Author(name=author.name)
            session.add(author)
            await session.flush()
            return Author(id=author.id, name=author.name)
