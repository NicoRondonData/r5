# schemas.py
from typing import List, Optional

import strawberry

from app.models import Author, Book, Category


@strawberry.type
class AuthorType:
    id: Optional[int]
    name: str
    books: List["BookType"]


@strawberry.input
class InputAuthorType:
    name: str


@strawberry.type
class CategoryType:
    id: int
    name: str
    books: List["BookType"]


#


@strawberry.type
class BookType:
    id: int
    title: str
    subtitle: Optional[str]
    author_id: int
    author: Optional[AuthorType]
    category_id: int
    category: Optional[CategoryType]
    publication_date: str
    editor: str
    description: str
    image: Optional[str]