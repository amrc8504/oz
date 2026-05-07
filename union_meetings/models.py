from django.db import models


class UnionMeetingInfo(models.Model):
    meeting_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    agenda = models.TextField(blank=True)
    past_meeting_notes = models.TextField(blank=True)
    union_contacts = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Union Meeting Info"