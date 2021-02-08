from django.db import models
# from django.core.urlresolvers import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    ceo=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
        # return reverse('detail',kwargs={'pk':self.pk})


class Employee(models.Model):
    name=models.CharField(max_length=30)
    salary=models.FloatField()
    company=models.ForeignKey(Company,related_name="emp",on_delete=models.CASCADE)


