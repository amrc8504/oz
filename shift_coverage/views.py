from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ShiftCoveragePost
from notifications.models import Notification
from .forms import ShiftCoveragePostForm
from django.http import HttpResponseForbidden


@login_required
def coverage_list(request):
    posts = (
    ShiftCoveragePost.objects.filter(status="open")
    | ShiftCoveragePost.objects.filter(author=request.user)
    | ShiftCoveragePost.objects.filter(selected_user=request.user)
)

    if request.user.is_superuser:
        posts = ShiftCoveragePost.objects.all()

    posts = posts.distinct().order_by("-created_at")

    return render(request, "shift_coverage/coverage_list.html", {"posts": posts})


@login_required
def create_coverage_post(request):

    if request.method == "POST":

        form = ShiftCoveragePostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            return redirect("shift_coverage:list")

    else:

        form = ShiftCoveragePostForm()

    return render(
        request,
        "shift_coverage/coverage_create.html",
        {
            "form": form
        }
    )
    
@login_required
def coverage_detail(request, post_id):

    try:
        post = ShiftCoveragePost.objects.get(id=post_id)

    except ShiftCoveragePost.DoesNotExist:
        return render(
            request,
            "notifications/deleted_content.html"
        )

    allowed = (
        post.status == "open"
        or request.user == post.author
        or request.user == post.selected_user
        or request.user.is_superuser
    )

    if not allowed:
        return HttpResponseForbidden(
            "You are not allowed to view this post."
        )

    return render(
        request,
        "shift_coverage/coverage_detail.html",
        {
            "post": post
        }
    )
    
@login_required
def mark_interested(request, post_id):

    post = get_object_or_404(
        ShiftCoveragePost,
        id=post_id
    )

    if request.user != post.author:

        post.interested_users.add(request.user)

    return redirect("shift_coverage:list")

@login_required
def withdraw_interest(request, post_id):

    post = get_object_or_404(
        ShiftCoveragePost,
        id=post_id
    )

    post.interested_users.remove(request.user)

    return redirect("shift_coverage:list")

@login_required
def select_user(request, post_id, user_id):
    post = get_object_or_404(ShiftCoveragePost, id=post_id)

    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to do this.")

    selected_user = get_object_or_404(User, id=user_id)

    if selected_user in post.interested_users.all():
        post.selected_user = selected_user
        post.status = "covered"
        post.save()

        Notification.objects.create(
            user=selected_user,
            message=f"You were awarded the shift: {post.title}",
            link=f"/shift-coverage/{post.id}/"
        )

    return redirect("shift_coverage:list")

@login_required
def close_post(request, post_id):
    post = get_object_or_404(ShiftCoveragePost, id=post_id)

    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to do this.")

    post.status = "cancelled"
    post.save()

    return redirect("shift_coverage:list")

@login_required
def edit_coverage_post(request, post_id):
    post = get_object_or_404(ShiftCoveragePost, id=post_id)

    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to edit this ticket.")

    if request.method == "POST":
        form = ShiftCoveragePostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("shift_coverage:list")
    else:
        form = ShiftCoveragePostForm(instance=post)

    return render(
        request,
        "shift_coverage/coverage_edit.html",
        {
            "form": form,
            "post": post,
        },
    )
    
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ShiftCoveragePost, id=post_id)

    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to delete this ticket.")

    if request.method == "POST":
        post.delete()
        return redirect("shift_coverage:list")

    return redirect("shift_coverage:list")