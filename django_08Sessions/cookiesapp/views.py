from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    request.session.set_test_cookie()
    print("Cookies are set!")
    return HttpResponse("Cookies are set! IndexPage")

#PageCount App
def check_view(request):
    if request.session.test_cookie_worked():
        print("Cookies baked up in client's machine ! :LOL")

        if 'count' in request.COOKIES:
            print("Cookies Counter Code [Test]", request.COOKIES['count'])
            newcount = int(request.COOKIES['count'])+1
        else:
            newcount = 1
        response = render(request,"cookies.html",{"count":newcount})
        response.set_cookie('count',newcount)
        return response

#To check your cookies on chrome: chrome://settings/cookies/detail?site=127.0.0.1

#Cookies in action, Form handling

def homepage(request):
    return render(request,"nameform.html",{"form":form})

def dateTimeView(request):
    name = request.GET['name']


    response = render(request,"datetime.html",{"name":name})
    response.set_cookie('name',name)
    return response

def ageview(request):
    name = request.GET['name']
    response = render(request,"age.html",{"name":name})
    response.set_cookie('name',name)
    return response

def eduview(request):
    age = request.GET['age']
    name = request.COOKIES['name']
    response = render(request,"edu.html",{"name":name})
    response.set_cookie('age',age,max_age=5)
    return response

def resultView(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    date_time = datetime.datetime.now()
    edu= request.GET['edu']
    data = {"datetime":date_time,"name":name,"age":age,"edu":edu}
    response = render(request,"result.html",{"data":data})
    response.set_cookie('edu', edu)
    return response