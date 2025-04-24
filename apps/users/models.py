from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='cover_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    job_role = models.CharField(max_length=100, blank=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Automatically create or update UserProfile when a User instance is created or updated.
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
 