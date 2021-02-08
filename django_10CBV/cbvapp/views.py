from django.shortcuts import render, HttpResponse
from django.views.generic import *

# Create your views here.
from .models import *


class HelloWorld(View):
    def get(self,request):
        return HttpResponse("<h1> Hello from Class Based View</h1>")

class TemplateCBV(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="Chetan"
        context['education']="BTech CSE"
        return context

class EmployeeView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = "cbvapp/employees.html"


def addemployee(request):
    emp = Employee()
    emp.name="Chetan"
    emp.company=Company.objects.get(pk=1)
    emp.salary=68000.00
    emp.location="Bangalore"
    emp.save()

def addcompanies(request):
    emp = Company()
    emp.name="Google"
    emp.location="L.A"
    emp.ceo="Sundar Pichai"
    emp.save()

class CompanyView(ListView):
    model = Company
    context_object_name = "companies"
    template_name = "cbvapp/companies.html"

class CompanyDetailView(DetailView):
    model = Company
    context_object_name = "company"
    template_name = "cbvapp/company_detail.html"


