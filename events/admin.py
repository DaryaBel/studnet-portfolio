from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Events, StudentsInEvents

class ParticipantsInline(admin.StackedInline):
    model = StudentsInEvents
    extra = 1

class EventsResource(resources.ModelResource): 
    class Meta:
        model = Events

class EventsAdmin(ImportExportModelAdmin):
    list_display = ("name", "date", "location")
    search_fields = ("name",)
    inlines = [ParticipantsInline]
    resource_class = EventsResource

class StudentsInEventsResource(resources.ModelResource): 
    class Meta:
        model = StudentsInEvents

class StudentsInEventsAdmin(ImportExportModelAdmin):
    list_display = ("student", "event", "role")
    list_filter = ("role",)
    resource_class = StudentsInEventsResource

admin.site.register(Events, EventsAdmin)
admin.site.register(StudentsInEvents, StudentsInEventsAdmin)
