from django.shortcuts import render, HttpResponse
from django.views.generic import *
# Create your views here.
from .models import *
from django.urls import *

class CompanyView(ListView):
    model = Company
    template_name = "cbvcrudapp/companies.html"

class CompanyDetailView(DetailView):
    model = Company
    template_name = "cbvcrudapp/company_detail.html"

class CompanyCreateView(CreateView):
    model = Company
    fields = ('name','location','ceo')


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name','location','ceo')

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('co')