from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .models import Projects
from .serializers import CreateTeamSerializer, CreateProjectSerializer, ProjectListSerializer, ProjectDetailSerializer

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

# Создание новой команды
class CreateTeamView(APIView):
    def post(self, request):
        serializer = CreateTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)

# Создание нового проекта
class CreateProjectView(APIView):
    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=201)