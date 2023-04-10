import strawberry

from app.graphql.resolvers import AuthorMutation, AuthorQuery


@strawberry.type
class Query(AuthorQuery):
    pass


@strawberry.type
class Mutation(AuthorMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
