from django import forms

class ItemAdd(forms.Form):
    itemName = forms.CharField()
    price = forms.FloatField()
