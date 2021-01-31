from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    sid = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    score = models.IntegerField()