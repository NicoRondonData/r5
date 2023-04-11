from sqlalchemy import Text, or_, select
from sqlalchemy.orm import joinedload

from app.db import get_session
from app.graphql.types import OreillyBookType
from app.models import Author, Book, Category
from app.oreilly.service import get_books_oreilly


async def fetch_local_books(term):
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


async def fetch_oreilly_books(term):
    results_oreilly = await get_books_oreilly(term)
    oreilly_books = []
    for i in results_oreilly:
        oreilly_books.append(
            OreillyBookType(
                archive_id=i.get("archive_id", ""),
                title=i.get("title", ""),
                description=i.get("description", ""),
                cover_url=i.get("cover_url", ""),
                authors=i.get("authors", []),
            )
        )
    return oreilly_books
