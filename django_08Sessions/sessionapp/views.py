import datetime

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def pagecount(request):
    count = request.session.get('count',0)
    ncount = count + 1
    request.session['count'] = ncount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,"pagecount.html",{'count':ncount})


def homepage(request):
    return render(request,"nameform.html")

def dateTimeView(request):
    name = request.GET['name']
    response = render(request,"datetime.html",{"date":datetime.datetime.now(),"name":name})
    return response

def ageview(request):
    name = request.GET['name']
    response = render(request,"age.html",{"name":name})
    request.session['name']=name
    return response

def eduview(request):
    age = request.GET['age']
    name = request.session.get('name')
    response = render(request,"edu.html",{"name":name})
    request.session['age']=age
    return response

def resultView(request):
    name = request.session.get('name')
    age = request.session.get('age')
    date_time = datetime.datetime.now()
    edu= request.GET['edu']
    request.session['edu'] = edu
    edu = request.session.get('edu')
    data = {"datetime":date_time,"name":name,"age":age,"edu":edu}
    response = render(request,"result.html",{"data":data})
    request.session.set_expiry(5)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.modified)
    request.session.set_expiry(5)
    print(request.session.items())
    return response

def dataview(request):
    for key in request.session.keys():
        request.session[key]
    print(request.session.items())
    return HttpResponse("<h1>All Sessions Cleared</h1>")