from django import forms
from . models import Movie
from django.core import validators
class DateInput(forms.DateInput):
    input_type = 'date'

ratings = (('','select rating'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),)

class MovieForm(forms.ModelForm):
    releaseDate = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    movieName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    starMale = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    starFemale = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    rating = forms.IntegerField(widget=forms.Select(choices=ratings,attrs={'class':'form-control'}),validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)])

    class Meta:
        model=Movie
        fields=['releaseDate','movieName','starMale','starFemale','rating']
