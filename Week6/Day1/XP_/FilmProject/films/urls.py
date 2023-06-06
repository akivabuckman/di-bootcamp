from django.contrib import admin
from django.urls import path, include
from .views import FilmCreateView, DirectorCreateView, FilmDeleteView, HomePageView, FavoriteFilmView

urlpatterns = [
    path('addFilm/', FilmCreateView.as_view(), name='create-film'),
    path('addDirector/', DirectorCreateView.as_view(), name='create-director'),
    path('addFilm/', FilmCreateView.as_view, name='create-film'),
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('deleteFilm/<pk>', FilmDeleteView.as_view(), name='delete-film'),
    path('favoriteFilm/<pk>', FavoriteFilmView.as_view(), name='favorite')
]