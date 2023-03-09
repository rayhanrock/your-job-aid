from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    resume = models.FileField(upload_to=user_directory_path, null=True)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance

    if created:
        profile = UserProfile(user=user)
        profile.save()