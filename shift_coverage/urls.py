from django.urls import path
from . import views

app_name = "shift_coverage"

urlpatterns = [

    path(
        "",
        views.coverage_list,
        name="list"
    ),

    path(
        "create/",
        views.create_coverage_post,
        name="create"
    ),
    
    path(
    "interested/<int:post_id>/",
    views.mark_interested,
    name="interested"
    ),
    
    path(
    "withdraw/<int:post_id>/",
    views.withdraw_interest,
    name="withdraw"
    ),
    
    path("edit/<int:post_id>/", views.edit_coverage_post, name="edit"),
    path("close/<int:post_id>/", views.close_post, name="close"),
    path("select/<int:post_id>/<int:user_id>/", views.select_user, name="select"),
    path(
    "<int:post_id>/",
    views.coverage_detail,
    name="detail"
    ),
    path("delete/<int:post_id>/", views.delete_post, name="delete"),
]