from typing import Optional

from pydantic import HttpUrl
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"
    id: Optional[int] = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255))
    books = relationship("Book", back_populates="author")


class Category(Base):
    __tablename__ = "category"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255))
    books = relationship("Book", back_populates="category")


class Book(Base):
    __tablename__ = "book"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(255))
    subtitle: str = Column(String(255), default=None, nullable=True)
    author_id: int = Column(Integer, ForeignKey("author.id"))
    author: Optional[Author] = relationship("Author", back_populates="books")
    category_id: int = Column(Integer, ForeignKey("category.id"))
    category: Optional[Category] = relationship("Category", back_populates="books")
    publication_date: str = Column(Date)
    editor: str = Column(String(255))
    description: str = Column(String(1000))
    image: Optional[HttpUrl] = Column(String, default=None, nullable=True)
