from typing import List

import strawberry
from sqlalchemy import Text, or_, select
from sqlalchemy.orm import joinedload

from app.db import get_session
from app.graphql.types import AuthorType, BookType, CategoryType
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
    async def search_books(self, term: str) -> List[BookType]:
        async with get_session() as session:
            statement = (
                select(Book)
                .options(joinedload(Book.author), joinedload(Book.category))
                .where(
                    or_(
                        Book.title.ilike(f"%{term}%"),
                        Book.subtitle.ilike(f"%{term}%"),
                        Book.author.has(Author.name.ilike(f"%{term}%")),
                        Book.category.has(Category.name.ilike(f"%{term}%")),
                        Book.publication_date.cast(Text).ilike(
                            f"%{term}%"
                        ),  # cast date to text
                        Book.editor.ilike(f"%{term}%"),
                        Book.description.ilike(f"%{term}%"),
                    )
                )
            )
            result = await session.execute(statement)
            records = result.scalars().all()
            return records
