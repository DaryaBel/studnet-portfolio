import graphene
from .types import UniversityType, FacultyType, SpecializationType, GroupsType, StudentType, EmployeeType, UserType, GroupType
from .models import Universities, Faculties, Specializations, Groups, Students, Employee 
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password

class CreateUniversityMutation(graphene.Mutation):
    class Arguments:
        fullname = graphene.String(required=True)
        shortname = graphene.String(required=True)
        location = graphene.String(required=True)
        description = graphene.String(required=True)
        
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, fullname, description, shortname, location):
        university = Universities.objects.create(
            fullname=fullname, description=description, shortname=shortname, location=location)

        return cls(ok=True)

class CreateFacultyMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        university = graphene.ID(required=True)
        description = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, university, description):
        universityObj = Universities.objects.get(pk=university)
        faculty = Faculties.objects.create(
            name=name, university=universityObj, description=description)

        return cls(ok=True)


class CreateSpecializationMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        faculty = graphene.ID(required=True)
        codeName = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, name, codeName, faculty):
        facultyObj = Faculties.objects.get(pk=faculty)
        specialization = Specializations.objects.create(
            name=name, faculty=facultyObj, codeName=codeName)

        return cls(ok=True)

class CreateGroupMutation(graphene.Mutation):
    class Arguments:
        course = graphene.Int(required=True)
        specialization = graphene.ID(required=True)
        codeName = graphene.String(required=True)
        formEducation = graphene.String(required=True)
        studyDegree = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, course, codeName, specialization, formEducation, studyDegree):
        specializationObj = Specializations.objects.get(pk=specialization)
        group = Groups.objects.create(
            course=course, formEducation=formEducation, studyDegree=studyDegree, specialization=specializationObj, codeName=codeName)

        return cls(ok=True)

class DeleteUniversityMutation(graphene.Mutation):
    class Arguments:
        university_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, university_id):
        university = Universities.objects.get(pk=university_id)
        university.delete()

        return cls(ok=True)


class DeleteFacultyMutation(graphene.Mutation):
    class Arguments:
        faculty_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, faculty_id):
        faculty = Faculties.objects.get(pk=faculty_id)
        faculty.delete()

        return cls(ok=True)


class DeleteSpecializationMutation(graphene.Mutation):
    class Arguments:
        specialization_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, specialization_id):
        specialization = Specializations.objects.get(pk=specialization_id)
        specialization.delete()

        return cls(ok=True)

class DeleteGroupMutation(graphene.Mutation):
    class Arguments:
        group_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, group_id):
        group = Groups.objects.get(pk=group_id)
        group.delete()

        return cls(ok=True)

class UpdateUniversityMutation(graphene.Mutation):
    class Arguments:
        university_id = graphene.ID(required=True)
        fullname = graphene.String(required=True)
        location = graphene.String(required=True)
        description = graphene.String(required=True)
        
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, fullname, description, location, university_id):
        university = Universities.objects.get(pk=university_id)
        university.fullname = fullname
        university.description = description
        university.location = location
        university.save()
        
        return cls(ok=True)
    
class UpdateFacultyMutation(graphene.Mutation):
    class Arguments:
        faculty_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        university = graphene.ID(required=True)
        description = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, faculty_id, name, university, description):
        faculty = Faculties.objects.get(pk=faculty_id)
        faculty.name = name
        faculty.description = description
        if int(university) != 0:
                universityObj = Universities.objects.get(pk=university)
                faculty.university = universityObj
        faculty.save()
        return cls(ok=True)


class UpdateSpecializationMutation(graphene.Mutation):
    class Arguments:
        specialization_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        faculty = graphene.ID(required=True)
        codeName = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, specialization_id, name, codeName, faculty):
        specialization = Specializations.objects.get(pk=specialization_id)
        specialization.name = name
        specialization.codeName = codeName
        if int(faculty) != 0:
                facultyObj = Faculties.objects.get(pk=faculty)
                specialization.faculty = facultyObj
        specialization.save()
        return cls(ok=True)

class UpdateGroupMutation(graphene.Mutation):
    class Arguments:
        group_id = graphene.ID(required=True)
        course = graphene.Int(required=True)
        specialization = graphene.ID(required=True)
        codeName = graphene.String(required=True)
        formEducation = graphene.String(required=True)
        studyDegree = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, course, group_id, codeName, specialization, formEducation, studyDegree):
        group = Groups.objects.get(pk=group_id)
        group.codeName = codeName
        group.formEducation = formEducation
        group.studyDegree = studyDegree
        group.course = course
        if int(specialization) != 0:
                specializationObj = Specializations.objects.get(pk=specialization)
                group.specialization = specializationObj
        group.save()
        return cls(ok=True)

class AuthMutation(graphene.Mutation):
    class Arguments:
        login = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)
    user_group = graphene.Field(GroupType)
    employee = graphene.Field(EmployeeType)
    is_ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info,  login, password):
        try:
            user = User.objects.get(username=login)
            is_ok = check_password(password, user.password)
            if not is_ok:
                return AuthMutation(user=None, user_group=None, employee=None, is_ok=is_ok)
            user_group = Group.objects.get(user=user)
            employee = Employee.objects.get(user=user)
            return AuthMutation(user=user,user_group=user_group, employee=employee, is_ok=is_ok)
        except User.DoesNotExist:
            user = None
            return AuthMutation(user=None, user_group=None, employee=None, is_ok=False)