from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Employee, Universities, Faculties, Specializations, Groups, Students

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

class UniversitiesResource(resources.ModelResource): 
    class Meta:
        model = Universities

class UniversitiesAdmin(ImportExportModelAdmin):
    list_display = ("fullname",)
    list_filter = ("location",)
    search_fields = ("fullname", "shortname")
    resource_class = UniversitiesResource

class FacultiesResource(resources.ModelResource): 
    class Meta:
        model = Faculties

class FacultiesAdmin(ImportExportModelAdmin):
    list_display = ("name", "university")
    search_fields = ("name", "university_id__fullname")
    resource_class = FacultiesResource

class SpecializationsResource(resources.ModelResource): 
    class Meta:
        model = Specializations

class SpecializationsAdmin(ImportExportModelAdmin):
    list_display = ("codeName", "name", "faculty")
    list_display_links = ("name",)
    search_fields = ("codeName", "name")
    resource_class = SpecializationsResource

class GroupsResource(resources.ModelResource): 
    class Meta:
        model = Groups

class GroupsAdmin(ImportExportModelAdmin):
    list_display = ("codeName", "specialization")
    list_filter = ("course", "formEducation", "studyDegree", "specialization_id__name")
    search_fields = ("codeName",)
    resource_class = GroupsResource

class StudentsResource(resources.ModelResource): 
    class Meta:
        model = Students

class StudentsAdmin(ImportExportModelAdmin):
    list_display = ("fullname", "group", "budgetary")
    list_filter = ("budgetary", "group_id__codeName")
    search_fields = ("fullname",)
    actions = ["makeBudgetary", "makeUnbudgetary"]
    resource_class = StudentsResource

    def makeUnbudgetary(self, request, queryset):
        # Перевести на коммерческое обучение
        row_update = queryset.update(budgetary=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def makeBudgetary(self, request, queryset):
        # Перевести на бюджетное обучение
        row_update = queryset.update(budgetary=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    makeBudgetary.short_description = "Перевести на бюджетное обучение"
    makeBudgetary.allowed_permissions = ('change', )

    makeUnbudgetary.short_description = "Перевести на коммерческое обучение"
    makeUnbudgetary.allowed_permissions = ('change', )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(Faculties, FacultiesAdmin)
admin.site.register(Specializations, SpecializationsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)

admin.site.site_title = "Портфолио студентов"
admin.site.site_header = "Портфолио студентов"
