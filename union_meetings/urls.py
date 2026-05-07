from django.urls import path
from . import views

app_name = "union_meetings"

urlpatterns = [
    path("", views.meetings_home, name="home"),
    path("edit/", views.edit_meeting_info, name="edit"),
]