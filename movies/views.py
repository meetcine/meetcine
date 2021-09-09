from django.views.generic import ListView, View
from django.http import Http404
from django.shortcuts import render
from . import models


class HomeView(ListView):
    model = models.Movie
    paginate_by = 2
    #paginate_orphans = 1
    ordering = "-created"

class RandomView(ListView):
    model = models.Movie
    paginate_by = 1
    template_name = "movies/random_list.html"
    
    def get_queryset(self):
        return models.Movie.objects.order_by('?')