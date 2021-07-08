from graphene_django import DjangoObjectType
from .models import Universities, Faculties, Specializations, Groups, Students, Employee
from django.contrib.auth.models import User, Group
import graphene

class UniversityType(DjangoObjectType):
    class Meta:
        model = Universities
        fields = "__all__"

class FacultyType(DjangoObjectType):
    class Meta:
        model = Faculties
        fields = "__all__"

class SpecializationType(DjangoObjectType):
    class Meta:
        model = Specializations
        fields = "__all__"

class GroupsType(DjangoObjectType):
    class Meta:
        model = Groups
        fields = "__all__"

class StudentType(DjangoObjectType):
    events_count = graphene.Int()
    teams_count = graphene.Int()

    class Meta:
        model = Students
        fields = "__all__"

    def resolve_events_count(self, info):
            return self.studentsInEvents.count()

    def resolve_teams_count(self, info):
            return self.studentsForTeam.count()


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = "__all__"

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = "__all__"
