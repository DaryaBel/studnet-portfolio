import graphene
from .types import ProjectType, TeamType 
from .models import Projects, Teams
from .mutation import AddToTeamMutation, CreateProjectMutation, CreateTeamMutation, CreateTeamWithPersonsMutation, DeleteProjectMutation, DeleteTeamMutation, UpdateProjectMutation, UpdateTeamMutation

class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, project_id=graphene.ID(required=True))

    all_teams = graphene.List(TeamType)
    team = graphene.Field(TeamType, team_id=graphene.ID(required=True))
    
    def resolve_all_projects(root, info):
        return Projects.objects.all()

    def resolve_project(root, info, project_id):
        return Projects.objects.get(pk=project_id)

    def resolve_all_teams(root, info):
        return Teams.objects.all()

    def resolve_team(root, info, team_id):
        return Teams.objects.get(pk=team_id)

class Mutation(graphene.ObjectType):
    create_project = CreateProjectMutation.Field()
    create_team = CreateTeamMutation.Field()
    create_team_with_persons = CreateTeamWithPersonsMutation.Field()
    delete_project = DeleteProjectMutation.Field()
    delete_team = DeleteTeamMutation.Field()
    update_team = UpdateTeamMutation.Field()
    add_to_team = AddToTeamMutation.Field()
    update_project  = UpdateProjectMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)    