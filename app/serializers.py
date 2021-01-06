from rest_framework import serializers
from .models import Students, Groups, Specializations, Faculties, Universities

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
