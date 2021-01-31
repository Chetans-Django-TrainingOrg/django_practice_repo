from django import forms
from django.core import validators


class SignUpForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(2)])
    emailId = forms.CharField(label="Email ID",validators=[validators.validate_email])
    pwd = forms.CharField(label="Password",widget=forms.PasswordInput)
    repwd = forms.CharField(label="Re-Enter Password",widget=forms.PasswordInput)

    def clean(self):
        all_clean_data = super().clean()
        pwd = all_clean_data["pwd"]
        repwd = all_clean_data["repwd"]
        if pwd != repwd:
            raise forms.ValidationError("The passwords didn't match.")


#a FORM to avoid BOT request
class SecureSignUpForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(2)])
    emailId = forms.CharField(label="Email ID",validators=[validators.validate_email])
    pwd = forms.CharField(label="Password",widget=forms.PasswordInput)
    repwd = forms.CharField(label="Re-Enter Password",widget=forms.PasswordInput)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        pwd = all_clean_data["pwd"]
        repwd = all_clean_data["repwd"]
        if pwd != repwd:
            raise forms.ValidationError("The passwords didn't match.")
        bot_handler = all_clean_data["bot_handler"]
        if len(bot_handler)>0:
            raise forms.ValidationError("Bots are not allowed !! Freeze. Now.")



