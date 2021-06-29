from graphene_django import DjangoObjectType
from .models import Events, StudentsInEvents
 
class EventType(DjangoObjectType):
    class Meta:
        model = Events
        fields = "__all__"

class StudentInEventType(DjangoObjectType):
    class Meta:
        model = StudentsInEvents
        fields = "__all__"
