from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    aggregate=models.FloatField()
    joindate = models.DateField()

