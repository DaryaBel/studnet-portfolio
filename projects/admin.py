from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Projects, Teams

class TeamsInline(admin.TabularInline):
    model = Teams
    extra = 1

class ProjectsResource(resources.ModelResource): 
    class Meta:
        model = Projects

class ProjectsAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [TeamsInline]
    save_on_top = True
    resource_class = ProjectsResource

class TeamsResource(resources.ModelResource): 
    class Meta:
        model = Teams

class TeamsAdmin(ImportExportModelAdmin):
    list_display = ("name", "project")
    search_fields = ("name", "project_id__name")
    resource_class = TeamsResource

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Teams, TeamsAdmin)
