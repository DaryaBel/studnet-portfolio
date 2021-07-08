import graphene
from .types import EventType, StudentInEventType 
from .models import Events, StudentsInEvents
from app.models import Students

class CreateEventMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        date = graphene.Date(required=True)
        location = graphene.String(required=True)
        description = graphene.String(required=True)
        
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, description, date, location):
        event = Events.objects.create(
            name=name, description=description, date=date, location=location)

        return cls(ok=True)


class CreateStudentInEventMutation(graphene.Mutation):
    class Arguments:
        student = graphene.ID(required=True)
        event = graphene.ID(required=True)
        role = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, student, event, role):
        studentObj = Students.objects.get(pk=student)
        eventObj = Events.objects.get(pk=event)
        studentInEvent = StudentsInEvents.objects.create(
            student=studentObj, event=eventObj, role=role)

        return cls(ok=True)

class DeleteEventMutation(graphene.Mutation):
    class Arguments:
        event_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, event_id):
        event = Events.objects.get(pk=event_id)
        event.delete()

        return cls(ok=True)


class DeleteStudentInEventMutation(graphene.Mutation):
    class Arguments:
        student_in_event_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, student_in_event_id):
        student_in_event = StudentsInEvents.objects.get(pk=student_in_event_id)
        student_in_event.delete()

        return cls(ok=True)

class UpdateEventMutation(graphene.Mutation):
    class Arguments:
        event_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        date = graphene.Date(required=True)
        location = graphene.String(required=True)
        description = graphene.String(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, description, date, location, event_id):
        event = Events.objects.get(pk=event_id)
        event.name = name
        event.description = description
        event.date = date
        event.location = location
        event.save()

        return cls(ok=True)

class UpdateStudentInEventMutation(graphene.Mutation):
    class Arguments:
        student_in_event_id = graphene.ID(required=True)
        student = graphene.ID(required=True)
        event = graphene.ID(required=True)
        role = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, student_in_event_id, student, event, role):
        studentInEvent = StudentsInEvents.objects.get(pk=student_in_event_id)
        if int(student) != 0:
                studentObj = Students.objects.get(pk=student)
                studentInEvent.student = studentObj
        if int(event) != 0:
                eventObj = Events.objects.get(pk=event)
                studentInEvent.event = eventObj
        studentInEvent.role = role        
        studentInEvent.save()
       
        return cls(ok=True)
