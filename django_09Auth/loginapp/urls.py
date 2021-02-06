from django.urls import path
from .views import *

urlpatterns = [
    path('home',Home_Page),
    path('cust',Customer),
    path('logout',Logout_View),
    path('homepage',homepage),
    path('python',pythonexams),
    path('java',javaexams),
    path('apti',aptiexams),
    path('logoutexams',logoutexams),
    path('signup',signup),

]