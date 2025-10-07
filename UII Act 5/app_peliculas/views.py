from django.shortcuts import render

# Create your views here.
from .models import Pelicula
def index (request):
    peliculas = Pelicula.objects.all()

    return render(request, 'index.html',{'peliculas': peliculas})