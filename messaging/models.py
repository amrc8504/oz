from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MessageThread(models.Model):
    participants = models.ManyToManyField(User, related_name="message_threads")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)