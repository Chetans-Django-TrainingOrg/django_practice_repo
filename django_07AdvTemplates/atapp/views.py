from django.shortcuts import render

# Create your views here.

def athandler(request):
    return render(request,'page1.html')