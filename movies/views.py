from django.http import HttpResponse
from django.shortcuts import render
from .models import movies

# Create your views here.
def index (request):
    movie_list = movies.objects.all()
    #output = ','.join([movie.title for movie in movie_list])
    return render(request, 'movies/index.html', {'movie_list': movie_list})