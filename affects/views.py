from django.views.generic import ListView, View
from django.shortcuts import render
from . import models
from movies.models import Movie

class AffectView(ListView):
    model = models.Affect
    
    def get_queryset(self):
        return models.Affect.objects.order_by('?')
    

def affect_detail(request, pk):
    movie = Movie.objects.all()
    affect = models.Affect.objects.get(pk=pk)
    movies = affect.movie_set.all()
    return render(request, "affects/affect_detail.html", {"affect":affect, "movies":movies})
    