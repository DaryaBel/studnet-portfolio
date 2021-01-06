from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>/", views.StudentDetailView.as_view()),
    path("events/", views.EventListView.as_view()),
    path("events/<int:pk>/", views.EventDetailView.as_view()),
    path("events/create/", views.CreateEventView.as_view()),
]