from rest_framework import serializers
from .models import Events, StudentsInEvents
from app.serializers import StudentListSerializer

# Вывод списка мероприятий
class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("id","name", "date")

# Получение студентов, участвовших в мероприятии
class StudentsInEventsSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()
    class Meta:
        model = StudentsInEvents
        fields = ("student", "role")

# Детальная информация о мероприятии
class EventDetailSerializer(serializers.ModelSerializer):
    eventsForStudent = StudentsInEventsSerializer(many=True)
    class Meta:
        model = Events
        fields = "__all__"

# Создание нового участника мероприятия
class CreateEventMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsInEvents
        fields = "__all__"
        

