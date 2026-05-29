from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import CustomLoginView

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path(
        "accounts/login/",
        CustomLoginView.as_view(),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("shift-coverage/", include("shift_coverage.urls")),
    path("discussions/", include("discussions.urls")),
    path("announcements/", include("announcements.urls")),
    path("messages/", include("messaging.urls")),
    path("profile/", include("profiles.urls")),
    path("notifications/", include("notifications.urls")),
    path("union-meetings/", include("union_meetings.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )