import pytest
from sqlmodel import SQLModel, create_engine

from app.models import Author, Book, Category


@pytest.fixture(name="database_url")
def database_url_fixture():
    return "sqlite:///:memory:"


@pytest.fixture(name="engine")
def engine_fixture(database_url):
    engine = create_engine(database_url)
    return engine


@pytest.fixture(name="create_tables")
def create_tables_fixture(engine):
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


def test_author_book_relationship(engine, create_tables):
    from sqlmodel import Session

    with Session(engine) as session:
        author = Author(name="John Doe")
        book = Book(
            title="Test Book",
            author_id=1,
            category_id=1,
            publication_date="2023-01-01",
            editor="Test Editor",
            description="A test book description.",
        )
        author.books = [book]

        session.add(author)
        session.commit()

        session.refresh(author)
        session.refresh(book)

        assert book.author_id == author.id
        assert book.author == author
        assert author.books[0] == book


def test_category_book_relationship(engine, create_tables):
    from sqlmodel import Session

    with Session(engine) as session:
        author = Author(name="Test Author")
        session.add(author)
        session.commit()
        session.refresh(author)

        category = Category(name="Fiction")
        session.add(category)
        session.commit()
        session.refresh(category)

        book = Book(
            title="Test Book",
            author_id=author.id,
            category_id=category.id,
            publication_date="2023-01-01",
            editor="Test Editor",
            description="A test book description.",
        )
        category.books = [book]

        session.add(book)
        session.commit()

        session.refresh(category)
        session.refresh(book)

        assert book.category_id == category.id
        assert book.category == category
        assert category.books[0] == book
