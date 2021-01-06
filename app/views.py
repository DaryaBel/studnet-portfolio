from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Students, Events
from .serializers import StudentListSerializer, StudentDetailSerializer, EventListSerializer, EventDetailSerializer, CreateEventSerializer

# Вывод списка студентов
class StudentListView(APIView):
    def get(self, request):
        # students = Students.objects.filter(budgetary=True)
        students = Students.objects
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data)

# Детальная информация о студенте
class StudentDetailView(APIView):
    def get(self, request, pk):
        student = Students.objects.get(id=pk)
        serializer = StudentDetailSerializer(student)
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
        # else:
        #     return Response(status=400)