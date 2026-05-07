from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Announcement
from .forms import AnnouncementForm


@login_required
def announcement_list(request):

    announcements = Announcement.objects.filter(
        approved=True
    ).order_by("-created_at")

    return render(
        request,
        "announcements/announcements_list.html",
        {
            "announcements": announcements
        }
    )


@login_required
def create_announcement(request):

    if request.method == "POST":

        form = AnnouncementForm(request.POST)

        if form.is_valid():

            announcement = form.save(commit=False)

            announcement.author = request.user

            if (
                request.user.is_superuser
                or request.user.groups.filter(
                    name="Union Representative"
                ).exists()
            ):
                announcement.approved = True
                announcement.reviewed_by = request.user

            else:
                announcement.approved = False

            announcement.save()

            return redirect("announcements:list")

    else:

        form = AnnouncementForm()

    return render(
    request,
    "announcements/create_announcement.html",
    {
        "form": form,
        "can_auto_approve": (
            request.user.is_superuser
            or request.user.groups.filter(
                name="Union Representative"
            ).exists()
        )
    }
)


@login_required
def pending_announcements(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    announcements = Announcement.objects.filter(
        approved=False
    ).order_by("-created_at")

    return render(
        request,
        "announcements/pending_announcements.html",
        {
            "announcements": announcements
        }
    )


@login_required
def approve_announcement(request, announcement_id):

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    announcement = get_object_or_404(
        Announcement,
        id=announcement_id
    )

    announcement.approved = True
    announcement.reviewed_by = request.user
    announcement.save()

    return redirect("announcements:pending")

@login_required
def reject_announcement(request, announcement_id):

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    announcement = get_object_or_404(
        Announcement,
        id=announcement_id
    )

    announcement.delete()

    return redirect("announcements:pending")

@login_required
def delete_announcement(request, announcement_id):

    announcement = get_object_or_404(
        Announcement,
        id=announcement_id
    )

    if request.user != announcement.author and not request.user.is_superuser:
        return HttpResponseForbidden(
            "You are not allowed to delete this announcement."
        )

    if request.method == "POST":
        announcement.delete()
        return redirect("announcements:list")

    return redirect("announcements:list")