from django.shortcuts import render
from datetime import date
# Create your views here.

def athandler(request):
    return render(request,'page1.html')

def movies(request):
    return render(request,'movies.html')

#add politics view too

def templateFilters(request):
    data = {"data":"somedata","date":date}
    return render(request,'filters.html',context={"data":data})