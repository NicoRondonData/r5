from app.repositories import AbstractRepository


class RepositoriesRegistry:
    def __init__(
        self,
        author_repository: AbstractRepository,
    ):
        self.author_repository = author_repository
