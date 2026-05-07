from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import (
    DiscussionPost,
    DiscussionComment,
    DiscussionVote,
)

from .forms import (
    DiscussionPostForm,
    DiscussionCommentForm,
)

from .models import (
    DiscussionPost,
    DiscussionComment,
    DiscussionVote,
    CommentVote,
)


@login_required
def discussion_list(request):

    posts = DiscussionPost.objects.all().order_by("-created_at")

    return render(
        request,
        "discussions/discussion_list.html",
        {
            "posts": posts
        }
    )


@login_required
def create_post(request):

    if request.method == "POST":

        form = DiscussionPostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect("discussions:list")

    else:

        form = DiscussionPostForm()

    return render(
        request,
        "discussions/create_post.html",
        {
            "form": form
        }
    )


@login_required
def post_detail(request, post_id):

    post = get_object_or_404(
        DiscussionPost,
        id=post_id
    )

    comments = post.comments.filter(
        parent__isnull=True
    ).order_by("created_at")

    if request.method == "POST":

        comment_form = DiscussionCommentForm(request.POST)

        if comment_form.is_valid():

            comment = comment_form.save(commit=False)

            comment.post = post
            comment.author = request.user

            parent_id = request.POST.get("parent_id")

            if parent_id:

                parent_comment = get_object_or_404(
                    DiscussionComment,
                    id=parent_id,
                    post=post
                )

                comment.parent = parent_comment

            comment.save()

            return redirect(
                "discussions:detail",
                post_id=post.id
            )

    else:

        comment_form = DiscussionCommentForm()

    return render(
        request,
        "discussions/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        }
    )
    
@login_required
def vote_post(request, post_id, vote_type):
    post = get_object_or_404(DiscussionPost, id=post_id)

    if vote_type == "up":
        value = DiscussionVote.UPVOTE
    elif vote_type == "down":
        value = DiscussionVote.DOWNVOTE
    else:
        return redirect("discussions:detail", post_id=post.id)

    vote, created = DiscussionVote.objects.get_or_create(
        post=post,
        user=request.user,
        defaults={"value": value}
    )

    if not created:
        if vote.value == value:
            vote.delete()
        else:
            vote.value = value
            vote.save()

    return redirect("discussions:detail", post_id=post.id)

@login_required
def vote_comment(request, comment_id, vote_type):

    comment = get_object_or_404(
        DiscussionComment,
        id=comment_id
    )

    if vote_type == "up":
        value = CommentVote.UPVOTE

    elif vote_type == "down":
        value = CommentVote.DOWNVOTE

    else:
        return redirect(
            "discussions:detail",
            post_id=comment.post.id
        )

    vote, created = CommentVote.objects.get_or_create(
        comment=comment,
        user=request.user,
        defaults={"value": value}
    )

    if not created:

        if vote.value == value:

            vote.delete()

        else:

            vote.value = value
            vote.save()

    return redirect(
        "discussions:detail",
        post_id=comment.post.id
    )
    
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id)

    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        post.delete()
        return redirect("discussions:list")

    return redirect("discussions:detail", post_id=post.id)