from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notification_list(request):

    notifications = request.user.notifications.all().order_by("-created_at")

    unread_count = request.user.notifications.filter(
        is_read=False
    ).count()

    return render(
        request,
        "notifications/notification_list.html",
        {
            "notifications": notifications,
            "unread_count": unread_count,
        }
    )

@login_required
def mark_notification_read(request, notification_id):

    notification = get_object_or_404(
        Notification,
        id=notification_id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    return redirect("notifications:list")

@login_required
def view_notification(request, notification_id):

    notification = get_object_or_404(
        Notification,
        id=notification_id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    if not notification.link:
        return render(
            request,
            "notifications/deleted_content.html"
        )

    return redirect(notification.link)