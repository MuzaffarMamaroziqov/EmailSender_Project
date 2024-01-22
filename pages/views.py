from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Album, Song

class AlbumView(ListView):
    model=Album
    template_name = 'home.html'


class SongView(TemplateView):
    model=Song
    template_name = 'about.html'

