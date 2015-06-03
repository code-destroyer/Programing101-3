from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    projections = {}
    for movie in movies:
        projections[movie] = movie.projection_set.all()
    return render(request, "index.html", locals())
