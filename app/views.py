from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teams, Projects, Students, Events, Groups, Specializations, Faculties, Universities, StudentsInEvents
from .serializers import CreateProjectSerializer, AddParticipantTeamProjectSerializer, ProjectListSerializer, ProjectDetailSerializer, UniversityListSerializer, UniversityDetailSerializer, FacultyDetailSerializer, FacultyListSerializer, SpecializationListSerializer, SpecializationDetailSerializer, GroupDetailSerializer, GroupListSerializer, StudentListSerializer, StudentDetailSerializer, EventListSerializer, EventDetailSerializer, CreateEventMemberSerializer

# Вывод списка студентов
class StudentListView(APIView):
    def get(self, request):
        students = Students.objects
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data)

# Детальная информация о студенте
class StudentDetailView(APIView):
    def get(self, request, pk):
        student = Students.objects.get(id=pk)
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)


# Вывод списка групп
class GroupListView(APIView):
    def get(self, request):
        groups = Groups.objects
        serializer = GroupListSerializer(groups, many=True)
        return Response(serializer.data)

# Детальная информация о группе
class GroupDetailView(APIView):
    def get(self, request, pk):
        group = Groups.objects.get(id=pk)
        serializer = GroupDetailSerializer(group)
        return Response(serializer.data)

# Вывод списка специальностей
class SpecializationListView(APIView):
    def get(self, request):
        specializations = Specializations.objects
        serializer = SpecializationListSerializer(specializations, many=True)
        return Response(serializer.data)

# Детальная информация о специальности
class SpecializationDetailView(APIView):
    def get(self, request, pk):
        specialization = Specializations.objects.get(id=pk)
        serializer = SpecializationDetailSerializer(specialization)
        return Response(serializer.data)

# Вывод списка факультетов
class FacultyListView(APIView):
    def get(self, request):
        faculties = Faculties.objects
        serializer = FacultyListSerializer(faculties, many=True)
        return Response(serializer.data)

# Детальная информация о факультетах
class FacultyDetailView(APIView):
    def get(self, request, pk):
        faculty = Faculties.objects.get(id=pk)
        serializer = FacultyDetailSerializer(faculty)
        return Response(serializer.data)

# Вывод списка университетов
class UniversityListView(APIView):
    def get(self, request):
        universities = Universities.objects
        serializer = UniversityListSerializer(universities, many=True)
        return Response(serializer.data)

# Детальная информация об университетах
class UniversityDetailView(APIView):
    def get(self, request, pk):
        university = Universities.objects.get(id=pk)
        serializer = UniversityDetailSerializer(university)
        return Response(serializer.data)

# Вывод списка мероприятий
class EventListView(APIView):
    def get(self, request):
        events = Events.objects
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

# Детальная информация о мероприятии
class EventDetailView(APIView):
    def get(self, request, pk):
        event = Events.objects.get(id=pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)

# Создание нового участника мероприятия
class CreateEventMemberView(APIView):
    def post(self, request):
        serializer = CreateEventMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)

# Вывод списка проектов
class ProjectListView(APIView):
    def get(self, request):
        projects = Projects.objects
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

# Детальная информация о проектах
class ProjectDetailView(APIView):
    def get(self, request, pk):
        project = Projects.objects.get(id=pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)


## НЕ ГОТОВО
# Команда проекта (добавление участника /  создание новой)
class AddParticipantTeamProjectView(APIView):
    def post(self, request):
        serializer = AddParticipantTeamProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

# Создание нового проекта
class CreateProjectView(APIView):
    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)