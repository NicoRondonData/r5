from typing import List, Optional

from pydantic import HttpUrl
from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str = Field(max_length=255)
    books: List["Book"] = Relationship(back_populates="author")


class Category(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(max_length=255)
    books: List["Book"] = Relationship(back_populates="category")


class Book(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str = Field(max_length=255)
    subtitle: str = Field(max_length=255, default=None, nullable=True)
    author_id: int = Field(foreign_key="author.id")
    author: Optional[Author] = Relationship(back_populates="books")
    category_id: int = Field(foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="books")
    publication_date: str = Field()
    editor: str = Field(max_length=255)
    description: str = Field(max_length=1000)
    image: Optional[HttpUrl] = Field(default=None, nullable=True)
