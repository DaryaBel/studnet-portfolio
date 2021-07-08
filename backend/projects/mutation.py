from app.models import Students
import graphene
from .types import ProjectType, TeamType 
from .models import Projects, Teams

class CreateProjectMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        dateStart = graphene.Date(required=True)
        dateEnd = graphene.Date(required=True)
        links = graphene.String(required=True)
    
    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, description, dateStart, dateEnd, links):
        project = Projects.objects.create(
            name=name, description=description, dateStart=dateStart, dateEnd=dateEnd, links=links)

        return CreateProjectMutation(project=project)

class DeleteProjectMutation(graphene.Mutation):
    class Arguments:
        project_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, project_id):
        project = Projects.objects.get(pk=project_id)
        project.delete()

        return cls(ok=True)

class DeleteTeamMutation(graphene.Mutation):
    class Arguments:
        team_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, team_id):
        team = Teams.objects.get(pk=team_id)
        team.delete()

        return cls(ok=True)

class CreateTeamMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        project = graphene.ID(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, project):
        projectObj = Projects.objects.get(pk=project)
        team = Teams.objects.create(
            name=name, project=projectObj)
        return cls(ok=True)


class CreateTeamWithPersonsMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        project = graphene.ID(required=True)
        participants = graphene.List(graphene.ID)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, project, participants):
        projectObj = Projects.objects.get(pk=project)
        team = Teams.objects.create(
            name=name, project=projectObj)
        participantsObj = Students.objects.filter(pk__in=participants)
        team.participants.set(participantsObj)
        team.save()
        return cls(ok=True)


class AddToTeamMutation(graphene.Mutation):
    class Arguments:
        team_id = graphene.ID(required=True)
        participants = graphene.List(graphene.ID)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, team_id, participants):
        team = Teams.objects.get(pk=team_id)
        participantsObj = Students.objects.filter(pk__in=participants)
        team.participants.set(participantsObj)
        team.save()
        return cls(ok=True)


class UpdateTeamMutation(graphene.Mutation):
    class Arguments:
        team_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        project = graphene.ID(required=True)
        
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, project, team_id):
        team = Teams.objects.get(pk=team_id)
        if int(project) != 0:
                projectObj = Projects.objects.get(pk=project)
                team.project = projectObj
        team.name = name        
        team.save()
        
        return cls(ok=True)

class UpdateProjectMutation(graphene.Mutation):
    class Arguments:
        project_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        dateStart = graphene.Date(required=True)
        dateEnd = graphene.Date(required=True)
        links = graphene.String(required=True)
        
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, description, dateStart, dateEnd, links, project_id):
        project = Projects.objects.get(pk=project_id)
        project.name = name
        project.description = description
        project.dateStart = dateStart
        project.dateEnd = dateEnd
        project.links = links        
        project.save()
        
        return cls(ok=True)
