"""django_10CBV URL Configuration

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
from cbvapp import views as cbvv
from cbvcrudapp import views as cbvcrudv
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', cbvv.HelloWorld.as_view()),
    path('templateview/', cbvv.TemplateCBV.as_view()),
    path('employee/', cbvv.EmployeeView.as_view()),
    path('addemployee/', cbvv.addemployee),
    path('companies/', cbvv.CompanyView.as_view()),

# Info about RegEx : https://www.regular-expressions.info/refext.html#:~:text=no-,no,must%20start%20with%20a%20letter.
# P stands for Placeholder or Pattern
#     url(r'^(?P<pk>\d+)/$', cbvv.CompanyDetailView.as_view(),name='detail1'),
    path('addco/', cbvv.addcompanies),

    #crud urls
    url(r'^(?P<pk>\d+)/$', cbvcrudv.CompanyDetailView.as_view(),name='detail'),
    path('addcompany', cbvcrudv.CompanyCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', cbvcrudv.CompanyUpdateView.as_view()),
    path('co/', cbvcrudv.CompanyView.as_view(),name='co'),
    url(r'^delete/(?P<pk>\d+)/$', cbvcrudv.CompanyDeleteView.as_view(),name='delete'),


]
