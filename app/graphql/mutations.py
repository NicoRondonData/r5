import strawberry

from app.db import get_session
from app.graphql.types import CategoryType  # noqa
from app.graphql.types import InputAuthorType  # noqa
from app.graphql.types import InputBookType  # noqa
from app.graphql.types import AuthorType, BookType, InputCategoryType
from app.models import Author, Book, Category


@strawberry.type
class BookMutation:
    @strawberry.mutation
    async def create_book(self, book: InputBookType) -> BookType:
        async with get_session() as session:
            new_book = Book(
                title=book.title,
                subtitle=book.subtitle,
                author_id=book.author_id,
                category_id=book.category_id,
                publication_date=book.publication_date,
                editor=book.editor,
                description=book.description,
                image=book.image,
            )
            session.add(new_book)
            await session.commit()
            await session.refresh(new_book)
            author = await session.get(Author, new_book.author_id)
            category = await session.get(Category, new_book.category_id)

            author_type = AuthorType(id=author.id, name=author.name)
            category_type = CategoryType(id=category.id, name=category.name)
            return BookType(
                id=new_book.id,
                title=new_book.title,
                subtitle=new_book.subtitle,
                author=author_type,
                category=category_type,
                publication_date=new_book.publication_date,
                editor=new_book.editor,
                description=new_book.description,
                image=new_book.image,
            )

    @strawberry.mutation
    async def delete_book(self, id: int) -> str:
        async with get_session() as session:
            book = await session.get(Book, id)
            if book is None:
                return f"Book with ID {id} not found"
            await session.delete(book)
            await session.commit()
            return f"Book with ID {id} deleted successfully"


@strawberry.type
class AuthorMutation:
    @strawberry.mutation
    async def create_author(self, author: InputAuthorType) -> AuthorType:
        async with get_session() as session:
            author = Author(name=author.name)
            session.add(author)
            await session.flush()
            return Author(id=author.id, name=author.name)


@strawberry.type
class CategoryMutation:
    @strawberry.mutation
    async def create_category(self, category: InputCategoryType) -> CategoryType:
        async with get_session() as session:
            category = Category(name=category.name)
            session.add(category)
            await session.flush()
            return Category(id=category.id, name=category.name)
