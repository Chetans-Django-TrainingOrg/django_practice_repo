from django.shortcuts import render
from . forms import *

# Create your views here.

def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SignUpForm()
    return render(request,"signUpForm/signup.html",context={"form":form})

def secureSignUp(request):
    if request.method == "POST":
        form = SecureSignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SecureSignUpForm()
    return render(request,"signUpForm/signup.html",context={"form":form})