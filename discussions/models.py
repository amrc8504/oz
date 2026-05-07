from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DiscussionPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def score(self):
        return sum(vote.value for vote in self.votes.all())


class DiscussionComment(models.Model):
    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
    "self",
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name="replies"
    )
    
    @property
    def score(self):
        return sum(vote.value for vote in self.votes.all())


class DiscussionVote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1

    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=((UPVOTE, "Upvote"), (DOWNVOTE, "Downvote")))

    class Meta:
        unique_together = ("post", "user")
        
class CommentVote(models.Model):

    UPVOTE = 1
    DOWNVOTE = -1

    comment = models.ForeignKey(
        DiscussionComment,
        on_delete=models.CASCADE,
        related_name="votes"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    value = models.SmallIntegerField(
        choices=(
            (UPVOTE, "Upvote"),
            (DOWNVOTE, "Downvote"),
        )
    )

    class Meta:
        unique_together = ("comment", "user")