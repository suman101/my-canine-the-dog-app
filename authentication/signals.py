from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.contrib.auth import user_logged_in,user_logged_out
from .models import UserProfile


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# TO CHECK ONLINE AND OFF-LINE STATUS OF USERS

