from django.urls import path
from .views import AlbumView, SongView


urlpatterns=[
    path('', AlbumView.as_view(), name='home' ),
    path('about', SongView.as_view(), name='about')

]