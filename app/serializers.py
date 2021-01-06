from rest_framework import serializers
from .models import Students, Events, StudentsInEvents

# Список студентов
class StudentListSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(slug_field="codeName", read_only=True)
    class Meta:
        model = Students
        fields = ("fullname", "group")

# Детальная информация о студенте
class StudentDetailSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(slug_field="codeName", read_only=True)    
    class Meta:
        model = Students
        fields = "__all__"
    
# Вывод списка мероприятий
class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("name", "date")

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

# Создание нового мероприятия
class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"
        # fields = ("name", "location", "description", "date")

    # def create(self, validated_data):
    #     event = Events.objects.update_or_create(
    #         name=validated_data.get("name", None),
    #         location=validated_data.get("location", None),
    #         description=validated_data.get("description", None),
    #         date=validated_data.get("date", None))

    #         # defaults={"storyPoints": validated_data.get("storyPoints", None)})
    #     return event