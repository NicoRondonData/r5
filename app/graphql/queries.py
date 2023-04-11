import asyncio
from typing import List

import strawberry
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.db import get_session
from app.graphql.services import fetch_local_books, fetch_oreilly_books
from app.graphql.types import CategoryType  # noqa
from app.graphql.types import AuthorType, BookType, SearchResultType
from app.models import Author, Book, Category


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
class CategoryQuery:
    @strawberry.field
    async def all_categories(self) -> List[CategoryType]:
        async with get_session() as session:
            statement = select(Category)
            result = await session.execute(statement)
            records = result.scalars().all()
            return records


@strawberry.type
class BookQuery:
    @strawberry.field
    async def all_books(self) -> List[BookType]:
        async with get_session() as session:
            statement = select(Book).options(
                joinedload(Book.author), joinedload(Book.category)
            )
            result = await session.execute(statement)
            records = result.scalars().all()
            return records

    @strawberry.field
    async def search_books(self, term: str) -> SearchResultType:
        oreilly_books, local_books = await asyncio.gather(
            fetch_oreilly_books(term), fetch_local_books(term)
        )

        return SearchResultType(local_books=local_books, oreilly_books=oreilly_books)
