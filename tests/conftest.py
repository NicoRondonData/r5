import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.models import Base

DATABASE_URL = "sqlite:///./test.db"  # use a local SQLite database file


@pytest.fixture(scope="session")
def engine():
    if not database_exists(DATABASE_URL):
        create_database(DATABASE_URL)

    engine = create_engine(DATABASE_URL)

    yield engine

    drop_database(DATABASE_URL)


@pytest.fixture(scope="function")
def session(engine):
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)
