from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.ProjectListView.as_view()),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view()),
    path("projects/add-team/", views.AddParticipantTeamProjectView.as_view()),
    path("projects/new/", views.CreateProjectView.as_view()),
]