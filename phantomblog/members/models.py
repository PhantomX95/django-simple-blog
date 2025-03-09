from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/profile-pics/', default='images\profile.jpg')
    location = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    tiktok_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    x_link = models.URLField(max_length=200, blank=True, null=True)
    linkedin_link = models.URLField(max_length=200, blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    # Add a field to specify the blog writer
    is_writer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"