from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
#Password-Based Key Derivation Function 2 : PBKDF2 SHA 256 Algorithms ! Damn ! So Secure !

#Doc : https://passlib.readthedocs.io/en/stable/lib/passlib.hash.pbkdf2_digest.html#passlib.hash.pbkdf2_sha256
# more Doc : https://passlib.readthedocs.io/en/stable/narr/hash-tutorial.html
# wiki ? Yeah, here : https://en.wikipedia.org/wiki/PBKDF2

def Home_Page(request):
    return render(request,'home.html')

@login_required
def Customer(request):
    return render(request,'customer.html')

def Logout_View(request):
    return render(request, 'registration/logout.html')

def homepage(request):
    return render(request,"homepage.html")

@login_required
def javaexams(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
    return render(request,"java.html",{"username":username})


@login_required
def pythonexams(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
    return render(request,"python.html",{"username":username})
    # return render(request,"python.html")


@login_required
def aptiexams(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
    return render(request,"apti.html",{"username":username})
    # return render(request,"apti.html")

def logoutexams(request):
    return render(request,"logout.html")

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            print("USER =",user.__dict__)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login")
    return render(request,"signup.html",{"form":form})