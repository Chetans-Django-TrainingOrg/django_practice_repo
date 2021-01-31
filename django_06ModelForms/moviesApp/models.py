from django.db import models

# Create your models here.

class Movie(models.Model):
    releaseDate = models.DateField()
    movieName = models.CharField(max_length=30)
    starMale = models.CharField(max_length=30)
    starFemale = models.CharField(max_length=30)
    rating = models.IntegerField()
