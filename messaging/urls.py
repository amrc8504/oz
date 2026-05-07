from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("", views.messaging_view, name="messages"),
]