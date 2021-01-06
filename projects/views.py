from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .models import Projects
from .serializers import CreateProjectSerializer, AddParticipantTeamProjectSerializer, ProjectListSerializer, ProjectDetailSerializer

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