from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Relationships
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Fields
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    # ImageField is a type of field that stores an image.
    avatar = models.ImageField(upload_to='profile_pics', blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"
