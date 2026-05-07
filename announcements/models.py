from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_announcements"
    )
    created_at = models.DateTimeField(auto_now_add=True)