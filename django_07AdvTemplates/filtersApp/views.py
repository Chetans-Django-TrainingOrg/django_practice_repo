from django.shortcuts import render

# Create your views here.

def templateFilterDemo(request):
    data = {"name":"Chetan","age":"30","job":"SOFTWARE TRainer"}
    return render(request,"movies.html",context={"data":data})
