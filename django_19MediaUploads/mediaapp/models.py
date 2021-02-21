from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    profilepic = models.FileField(blank=True,null=True, upload_to="profilepics")
