from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>/", views.StudentDetailView.as_view()),
    path("groups/", views.GroupListView.as_view()),
    path("groups/<int:pk>/", views.GroupDetailView.as_view()),
    path("specializations/", views.SpecializationListView.as_view()),
    path("specializations/<int:pk>/", views.SpecializationDetailView.as_view()),
    path("faculties/", views.FacultyListView.as_view()),
    path("faculties/<int:pk>/", views.FacultyDetailView.as_view()),
    path("universities/", views.UniversityListView.as_view()),
    path("universities/<int:pk>/", views.UniversityDetailView.as_view()),
    ]