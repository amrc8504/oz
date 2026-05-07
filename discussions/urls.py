from django.urls import path
from . import views

app_name = "discussions"

urlpatterns = [

    path(
        "",
        views.discussion_list,
        name="list"
    ),

    path(
        "create/",
        views.create_post,
        name="create"
    ),

    path(
        "<int:post_id>/",
        views.post_detail,
        name="detail"
    ),
    path(
    "<int:post_id>/vote/<str:vote_type>/",
    views.vote_post,
    name="vote"),
    
    path(
    "comment/<int:comment_id>/vote/<str:vote_type>/",
    views.vote_comment,
    name="vote_comment"
    ),
    
    path("<int:post_id>/delete/", views.delete_post, name="delete"),
    
]