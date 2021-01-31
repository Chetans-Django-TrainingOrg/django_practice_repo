from django.shortcuts import render
from .forms import StudenForm
from django.shortcuts import redirect

# Create your views here.


def studentForm(request):
    if request.method=="POST":
        form = StudenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form = StudenForm()
    return render(request,"sform.html",context={"form":form})

def indexPage(request):
    return render(request,"done.html")