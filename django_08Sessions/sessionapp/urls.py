from django.urls import path
from . views import *

urlpatterns = [
    path('pagecount', pagecount),
    path('home', homepage),
    path('age', ageview),
    path('edu', eduview),
    path('result',resultView),
    path('data',dataview),
]