import graphene
import app.schema
import events.schema
import projects.schema

class Query(app.schema.Query, events.schema.Query, projects.schema.Query, graphene.ObjectType):
    pass

class Mutation(events.schema.Mutation, projects.schema.Mutation, app.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
