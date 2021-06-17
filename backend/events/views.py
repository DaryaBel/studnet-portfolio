from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .models import Events
from .serializers import EventListSerializer, EventDetailSerializer, CreateEventMemberSerializer

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

