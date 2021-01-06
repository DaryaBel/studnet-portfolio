from rest_framework import serializers
from .models import Teams, Projects, Students, Events, StudentsInEvents, Groups, Specializations, Faculties, Universities

# Список студентов
class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ("fullname",)

# Детальная информация о студенте
class StudentDetailSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(slug_field="codeName", read_only=True)    
    class Meta:
        model = Students
        fields = "__all__"

# Список групп
class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ("codeName",)
        
# Детальная информация о группе
class GroupDetailSerializer(serializers.ModelSerializer):
    specialization = serializers.SlugRelatedField(slug_field="name", read_only=True)
    studentsOfGroup = StudentListSerializer(many=True)
    class Meta:
        model = Groups
        fields = "__all__"

# Список специальностей
class SpecializationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializations
        fields = ("codeName", "name")
        
# Детальная информация о специальностях
class SpecializationDetailSerializer(serializers.ModelSerializer):
    faculty = serializers.SlugRelatedField(slug_field="name", read_only=True)    
    groupsOfSpecialization = GroupListSerializer(many=True)
    class Meta:
        model = Specializations
        fields = "__all__"

# Список факультетов
class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ("name",)
        
# Детальная информация о факультетах
class FacultyDetailSerializer(serializers.ModelSerializer):
    university = serializers.SlugRelatedField(slug_field="fullname", read_only=True)    
    specializationsOfFaculty = SpecializationListSerializer(many=True)
    class Meta:
        model = Faculties
        fields = "__all__"

# Список университетов
class UniversityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = ("fullname",)
        
# Детальная информация об университетах
class UniversityDetailSerializer(serializers.ModelSerializer):
    facultiesOfUniversity = FacultyListSerializer(many=True)
    class Meta:
        model = Universities
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

# Создание нового участника мероприятия
class CreateEventMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsInEvents
        fields = "__all__"
        

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

# Команда проекта (добавление участника /  создание новой)
class AddParticipantTeamProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"
    
    def create(self, validated_data):
        team = Teams.objects.update_or_create(
            name=validated_data.get("name", None),
            project=validated_data.get("project", None),
            defaults={"participants": validated_data.get("participants", None)})
        return team

# Создание нового проекта
class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"