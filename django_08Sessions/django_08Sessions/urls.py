"""django_08Sessions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cookiesapp import views as cookiesappViews
from cookieCart import views as cookieCartViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookieset/', cookiesappViews.index),
    path('cookietest/', cookiesappViews.check_view),
    path('nameform/', cookiesappViews.homepage),
    path('date/', cookiesappViews.dateTimeView),
    path('age/', cookiesappViews.ageview),
    path('edu/', cookiesappViews.eduview),
    path('result/', cookiesappViews.resultView),
    path('home/', cookieCartViews.home),
    path('add/', cookieCartViews.additem),
    path('display/', cookieCartViews.displayitems),
]
