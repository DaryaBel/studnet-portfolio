from django.contrib import admin
from .models import Universities, Faculties, Specializations, Groups, Students, Events, Projects, StudentsInEvents, Teams, StudentsInTeams

admin.site.register(Universities)
admin.site.register(Faculties)
admin.site.register(Specializations)
admin.site.register(Groups)
admin.site.register(Students)
admin.site.register(Events)
admin.site.register(Projects)
admin.site.register(StudentsInEvents)
admin.site.register(Teams)
admin.site.register(StudentsInTeams)