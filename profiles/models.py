from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True
    )

    @property
    def display_name(self):

        first = self.user.first_name.strip()

        last_initial = ""

        if self.user.last_name:
            last_initial = f"{self.user.last_name[0]}"

        if first and last_initial:
            return f"{first} {last_initial}"

        if first:
            return first

        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    UserProfile.objects.get_or_create(user=instance)
    instance.userprofile.save()