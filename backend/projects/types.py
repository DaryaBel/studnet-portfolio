from app.models import Students
import graphene
from graphene_django import DjangoObjectType
from .models import Projects, Teams
from app.types import StudentType
 
class ProjectType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = "__all__"

class TeamType(DjangoObjectType):
    participants = graphene.List(StudentType)

    class Meta:
        model = Teams
        fields = "__all__"
    
    def resolve_participants(self, info):
        ids = [participant.id for participant in self.participants.all()]
        return Students.objects.filter(pk__in=ids)
