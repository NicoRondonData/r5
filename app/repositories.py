from abc import ABC, abstractmethod

from pydantic.main import BaseModel
from sqlalchemy import select

from app.models import Author


class AbstractRepository(ABC):
    def __init__(self, session):
        self._session = session

    @abstractmethod
    async def add(self, author: str) -> BaseModel:
        pass

    @abstractmethod
    async def get_all(self):
        pass

    # @abstractmethod
    # async def get_by_field(self, search_text: str) -> List[BaseModel]:
    #     pass


class AuthorRepository(AbstractRepository):
    async def add(self, author: Author) -> Author:
        new_author = self._session.add(author)
        await self._session.flush()
        return new_author

    async def get_all(self):
        statement = select(Author)

        results = (await self._session.execute(statement)).all()
        return results
