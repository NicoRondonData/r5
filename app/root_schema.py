import strawberry

from app.graphql.mutations import BookMutation  # noqa
from app.graphql.mutations import AuthorMutation, CategoryMutation  # noqa
from app.graphql.queries import AuthorQuery, BookQuery, CategoryQuery


@strawberry.type
class Query(AuthorQuery, BookQuery, CategoryQuery):
    pass


@strawberry.type
class Mutation(AuthorMutation, CategoryMutation, BookMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
