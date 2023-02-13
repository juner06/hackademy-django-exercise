from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profilepicture = models.FileField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=250)