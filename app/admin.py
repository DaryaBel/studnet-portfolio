from django.contrib import admin
from .models import Universities, Faculties, Specializations, Groups, Students, Events, Projects, StudentsInEvents, Teams

class UniversitiesAdmin(admin.ModelAdmin):
    list_display = ("fullname",)
    list_filter = ("location",)
    search_fields = ("fullname", "shortname")

class FacultiesAdmin(admin.ModelAdmin):
    list_display = ("name", "university")
    search_fields = ("name", "university_id__fullname")

class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ("codeName", "name", "faculty")
    list_display_links = ("name",)
    search_fields = ("codeName", "name")

class GroupsAdmin(admin.ModelAdmin):
    list_display = ("codeName", "specialization")
    list_filter = ("course", "formEducation", "studyDegree", "specialization_id__name")
    search_fields = ("codeName",)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ("fullname", "group", "budgetary")
    list_filter = ("budgetary", "group_id__codeName")
    search_fields = ("fullname",)
    actions = ["makeBudgetary", "makeUnbudgetary"]

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


class ParticipantsInline(admin.StackedInline):
    model = StudentsInEvents
    extra = 1

class EventsAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "location")
    search_fields = ("name",)
    inlines = [ParticipantsInline]

class TeamsInline(admin.TabularInline):
    model = Teams
    extra = 1

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [TeamsInline]
    save_on_top = True

class StudentsInEventsAdmin(admin.ModelAdmin):
    list_display = ("student", "event", "role")
    list_filter = ("role",)

class TeamsAdmin(admin.ModelAdmin):
    list_display = ("name", "project")
    search_fields = ("name", "project_id__name")

admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(Faculties, FacultiesAdmin)
admin.site.register(Specializations, SpecializationsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(StudentsInEvents, StudentsInEventsAdmin)
admin.site.register(Teams, TeamsAdmin)

admin.site.site_title = "Портфолио студентов"
admin.site.site_header = "Портфолио студентов"
