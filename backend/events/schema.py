from .mutation import CreateEventMutation, CreateStudentInEventMutation, DeleteEventMutation, DeleteStudentInEventMutation, UpdateEventMutation, UpdateStudentInEventMutation
import graphene
from .types import EventType, StudentInEventType 
from .models import Events, StudentsInEvents

class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    event = graphene.Field(EventType, event_id=graphene.ID(required=True))

    all_students_in_events = graphene.List(StudentInEventType)
    student_in_event = graphene.Field(StudentInEventType, student_in_event_id=graphene.ID(required=True))
    
    def resolve_all_events(root, info):
        return Events.objects.all()

    def resolve_event(root, info, event_id):
        return Events.objects.get(pk=event_id)

    def resolve_all_students_in_events(root, info):
        return StudentsInEvents.objects.all()

    def resolve_student_in_event(root, info, student_in_event_id):
        return StudentsInEvents.objects.get(pk=student_in_event_id)

class Mutation(graphene.ObjectType):
    create_student_in_event = CreateStudentInEventMutation.Field()
    create_event = CreateEventMutation.Field()
    delete_student_in_event = DeleteStudentInEventMutation.Field()
    delete_event = DeleteEventMutation.Field()
    update_event = UpdateEventMutation.Field()
    update_student_in_event = UpdateStudentInEventMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)    