from django.shortcuts import render
from . forms import MovieForm
from  . models import Movie
# Create your views here.


def indexView(request):
    return render(request,"index.html")

def addMovie(request):
    if request.method=="POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            print("Added")
            form.save(commit=True)
            print("dont know")
            return indexView(request)
    else:
        form=MovieForm()
    return render(request,"addmovie.html",{'form':form})

def listMovies(request):
    moviesList = Movie.objects.all().order_by('rating')
    return render(request,'listmovies.html',{'movies':moviesList})
