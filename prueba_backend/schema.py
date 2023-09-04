import graphene

import academia.schema


class Query(academia.schema.Query, graphene.ObjectType):
    pass


class Mutation(academia.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
