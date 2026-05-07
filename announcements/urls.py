from django.urls import path
from . import views

app_name = "announcements"

urlpatterns = [

    path(
        "",
        views.announcement_list,
        name="list"
    ),

    path(
        "create/",
        views.create_announcement,
        name="create"
    ),

    path(
        "pending/",
        views.pending_announcements,
        name="pending"
    ),

    path(
        "approve/<int:announcement_id>/",
        views.approve_announcement,
        name="approve"
    ),
    
    path(
    "reject/<int:announcement_id>/",
    views.reject_announcement,
    name="reject"
    ),
    
    path(
    "delete/<int:announcement_id>/",
    views.delete_announcement,
    name="delete"
    ),
]