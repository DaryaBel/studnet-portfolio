from rest_framework import serializers
from .models import Teams, Projects

# Вывод списка проектов
class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("name",)

# Получение команд, прикрепленных к проекту
class TeamsSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(slug_field="fullname", read_only=True, many=True)    
    class Meta:
        model = Teams
        fields = "__all__"

# Детальная информация о проектах
class ProjectDetailSerializer(serializers.ModelSerializer):
    teamsForProject = TeamsSerializer(many=True)
    class Meta:
        model = Projects
        fields = "__all__"

# Создание новой команды
class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"

# Создание нового проекта
class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"