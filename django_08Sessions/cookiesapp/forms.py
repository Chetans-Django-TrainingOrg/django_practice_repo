from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), label="Name")

