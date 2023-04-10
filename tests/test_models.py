from datetime import date

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.models import Author, Base, Book, Category

DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="module")
def engine():
    if not database_exists(DATABASE_URL):
        create_database(DATABASE_URL)

    engine = create_engine(DATABASE_URL)

    yield engine

    drop_database(DATABASE_URL)


@pytest.fixture(scope="module")
def session(engine):
    Base.metadata.create_all(engine)
    session = Session(engine)

    yield session

    session.close()
    Base.metadata.drop_all(engine)


def test_author_and_book_relationship(session):
    author = Author(name="John Doe")
    session.add(author)
    session.commit()

    book = Book(
        title="Test Book",
        author_id=author.id,
        publication_date=date(2023, 4, 10),
        editor="Test Editor",
        description="Test Description",
        category_id=None,
    )
    session.add(book)
    session.commit()

    fetched_book = session.query(Book).filter(Book.id == book.id).one()
    fetched_author = session.query(Author).filter(Author.id == author.id).one()

    assert fetched_book.author.id == fetched_author.id
    assert fetched_book.author.name == "John Doe"
    assert fetched_author.books[0].title == "Test Book"


def test_category_and_book_relationship(session):
    category = Category(name="Fiction")
    session.add(category)
    session.commit()

    book = Book(
        title="Test Book 2",
        category_id=category.id,
        publication_date=date(2023, 4, 10),
        editor="Test Editor",
        description="Test Description",
        author_id=None,
    )
    session.add(book)
    session.commit()

    fetched_book = session.query(Book).filter(Book.id == book.id).one()
    fetched_category = session.query(Category).filter(Category.id == category.id).one()

    assert fetched_book.category.id == fetched_category.id
    assert fetched_book.category.name == "Fiction"
    assert fetched_category.books[0].title == "Test Book 2"
