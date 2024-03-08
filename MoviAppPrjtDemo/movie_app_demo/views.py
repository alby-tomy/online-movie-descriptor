from django.http import HttpResponse
from django.shortcuts import redirect, render

from movie_app_demo.forms import MovieForm
from . models import MovieDetails

# Create your views here.
def index(request):
    movie = MovieDetails.objects.all()
    context = {
        'movie_list' : movie
    }
    return render(request,'index.html',context)

def detailsView(request,movieId):
    movie_id = MovieDetails.objects.get(id=movieId)
    return render(request,'details.html',{'movie_Id':movie_id})

def addItems(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('descri')
        year = request.POST.get('year')
        img = request.FILES['image']

        movie = MovieDetails(name=name, description=description, year=year, img=img)
        movie.save()

    return render(request, 'add.html')

def updateField(request, movieId):
    movieID = MovieDetails.objects.get(id=movieId)
    formUpdate = MovieForm(request.POST or None, request.FILES, instance=movieID)
    if formUpdate.is_valid():
        formUpdate.save()
        return redirect('/')
    return render(request, 'update.html',{'form':formUpdate,'movieId':movieID})

def deleteData(request, movieId):
    if request.method == 'POST':
         movieID = MovieDetails.objects.get(id=movieId)
         movieID.delete()
         return redirect('/')
    return render(request,'delete.html')