from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.notification_list, name="list"),
    path(
    "read/<int:notification_id>/",
    views.mark_notification_read,
    name="read"
),
    path("view/<int:notification_id>/", views.view_notification, name="view"),
]