from django.contrib import admin
from django.urls import path, include
from .views import FilmCreateView, DirectorCreateView, HomePageView

urlpatterns = [
    path('addFilm/', FilmCreateView.as_view(), name='create-film'),
    path('addDirector/', DirectorCreateView.as_view(), name='create-director'),
    path('addFilm/', FilmCreateView.as_view, name='create-film'),
    path('homepage/', HomePageView.as_view(), name='homepage'),
]