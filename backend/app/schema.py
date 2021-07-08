from .mutation import AuthMutation, CreateFacultyMutation, CreateGroupMutation, CreateSpecializationMutation, CreateUniversityMutation, DeleteFacultyMutation, DeleteGroupMutation, DeleteSpecializationMutation, DeleteUniversityMutation, UpdateFacultyMutation, UpdateGroupMutation, UpdateSpecializationMutation, UpdateUniversityMutation
from collections import namedtuple
import graphene
from django.db.models import Sum, Count
from .types import UniversityType, FacultyType, SpecializationType, GroupsType, StudentType, EmployeeType, UserType
from .models import Universities, Faculties, Specializations, Groups, Students, Employee 
from django.contrib.auth.models import User

StudentStatisticsObject = namedtuple(
    "StudentStatisticsType", ["students"])

class StudentStatisticsType(graphene.ObjectType):
    students = graphene.List(StudentType)
    
class Query(graphene.ObjectType):
    all_universities = graphene.List(UniversityType)
    university = graphene.Field(UniversityType, university_id=graphene.ID(required=True))
    
    all_faculties = graphene.List(FacultyType)
    faculty = graphene.Field(FacultyType, faculty_id=graphene.ID(required=True))
    
    all_specializations = graphene.List(SpecializationType)
    specialization = graphene.Field(SpecializationType, specialization_id=graphene.ID(required=True))
    
    all_groups = graphene.List(GroupsType)
    group = graphene.Field(GroupsType, group_id=graphene.ID(required=True))

    all_students = graphene.List(StudentType)
    student = graphene.Field(StudentType, student_id=graphene.ID(required=True))

    all_employees = graphene.List(EmployeeType)
    employee = graphene.Field(EmployeeType, employee_id=graphene.ID(required=True))
    
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.ID(required=True))
    
    statistics = graphene.Field(StudentStatisticsType)

    def resolve_all_universities(root, info):
        return Universities.objects.all()

    def resolve_university(root, info, university_id):
        return Universities.objects.get(pk=university_id)

    def resolve_all_faculties(root, info):
        return Faculties.objects.all()

    def resolve_faculty(root, info, faculty_id):
        return Faculties.objects.get(pk=faculty_id)

    def resolve_all_specializations(root, info):
        return Specializations.objects.all()

    def resolve_specialization(root, info, specialization_id):
        return Specializations.objects.get(pk=specialization_id)
    
    def resolve_all_groups(root, info):
        return Groups.objects.all()
        
    def resolve_group(root, info, group_id):
        return Groups.objects.get(pk=group_id)

    def resolve_all_students(root, info):
        return Students.objects.all()

    def resolve_student(root, info, student_id):
        return Students.objects.get(pk=student_id)
    
    def resolve_all_employees(root, info):
        return Employee.objects.all()

    def resolve_employee(root, info, employee_id):
        return Employee.objects.get(pk=employee_id)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user(root, info, user_id):
        return User.objects.get(pk=user_id)

    def resolve_statistics(self, info):
        students = Students.objects.all()
        return StudentStatisticsObject(students=students)

class Mutation(graphene.ObjectType):
    create_university = CreateUniversityMutation.Field()
    create_faculty = CreateFacultyMutation.Field()
    create_specialization = CreateSpecializationMutation.Field()
    create_group = CreateGroupMutation.Field()
    delete_university = DeleteUniversityMutation.Field()
    delete_faculty = DeleteFacultyMutation.Field()
    delete_specialization = DeleteSpecializationMutation.Field()
    delete_group = DeleteGroupMutation.Field()
    update_university = UpdateUniversityMutation.Field()
    update_faculty = UpdateFacultyMutation.Field()
    update_specialization = UpdateSpecializationMutation.Field()
    update_group = UpdateGroupMutation.Field()
    auth = AuthMutation.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)    