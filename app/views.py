from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Students, Events, Groups, Specializations, Faculties, Universities
from .serializers import UniversityListSerializer, UniversityDetailSerializer, FacultyDetailSerializer, FacultyListSerializer, SpecializationListSerializer, SpecializationDetailSerializer, GroupDetailSerializer, GroupListSerializer, StudentListSerializer, StudentDetailSerializer, EventListSerializer, EventDetailSerializer, CreateEventSerializer

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

# Создание нового мероприятия
class CreateEventView(APIView):
    def post(self, request):
        serializer = CreateEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)