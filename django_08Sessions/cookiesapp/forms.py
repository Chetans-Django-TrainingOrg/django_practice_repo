from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), label="Name")

class AgeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), label="Age")

class DegreeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), label="Degree")

