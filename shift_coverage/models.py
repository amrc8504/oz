from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ShiftCoveragePost(models.Model):

    STATUS_CHOICES = [
        ("open", "Open"),
        ("covered", "Covered"),
        ("cancelled", "Cancelled"),
    ]

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="coverage_posts"
    )

    title = models.CharField(max_length=120)

    shift_date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    location = models.CharField(max_length=120, blank=True)

    note = models.TextField(blank=True)

    interested_users = models.ManyToManyField(
        User,
        blank=True,
        related_name="interested_coverage_posts"
    )

    selected_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="selected_coverage_posts"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def is_past_shift(self):
        return self.shift_date < timezone.now().date()

    def __str__(self):
        return self.title