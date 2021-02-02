from django.shortcuts import render
from .forms import ItemAdd
# Create your views here.

def home(request):
    return render(request,"home.html")

def additem(request):
    form = ItemAdd()
    response = render(request,"additem.html",{'form':form})
    if request.method=='POST':
        form=ItemAdd(request.POST)
        if form.is_valid():
            itemName = form.cleaned_data['itemName']
            price = form.cleaned_data['price']
            response.set_cookie(itemName,price)
    return response

def displayitems(request):
    return render(request,"showitems.html")