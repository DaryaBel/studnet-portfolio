from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventListView.as_view()),
    path("events/<int:pk>/", views.EventDetailView.as_view()),
    path("events/add-member/", views.CreateEventMemberView.as_view())
]