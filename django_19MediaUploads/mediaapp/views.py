import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *

def Home(request):
    return render(request,'home.html')

def AddNewStudent(request):
    form = ProfileForm(request.POST or None ,request.FILES or None )
    if form.is_valid():
        instance= form.save()
        instance.save()
        return HttpResponseRedirect('/')
    context={'form': form}
    return  render (request,"add.html",context)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        if "pdf" in myfile.name:
            fs = FileSystemStorage(location='media/pdfs')
        elif "docx" in myfile.name:
            fs = FileSystemStorage(location='media/docs')
        elif "jpg" in myfile.name or "jpeg" in myfile.name or "png" in myfile.name:
            fs = FileSystemStorage(location='media/images')
        else:
            fs = FileSystemStorage(location='media/others')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'fupload.html',{'uploaded_file_url': uploaded_file_url})
    return render(request, 'fupload.html')