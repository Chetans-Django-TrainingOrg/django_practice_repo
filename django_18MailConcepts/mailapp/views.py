from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def sending_mail():
    name= "Chethan"
    mail = "chetanfolk@gmail.com"
    sub = "Simple Hey"
    message = "Checked mail working in django"
    print("Sending")
    send_mail('got mail from'+str(mail),
        "name: "+str(name)+"\n"
        "email:"+str(mail)+"\n"
        "subject: "+str(sub)+"\n"
        "message :"+ str(message),
        settings.EMAIL_HOST_USER,
        ['chetuh10@gmail.com'],
        fail_silently=False )
    print("Sent")

sending_mail()

