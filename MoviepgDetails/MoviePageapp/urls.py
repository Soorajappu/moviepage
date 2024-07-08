from django.urls import path
from . import views

urlpatterns = [
    path('', views.moviepage),
    path('director/', views.director_create, name='director'),
    path('directors/', views.director_list, name='director_list'),
    path('movie/', views.movie_create, name='movie'),
    path('showlist/', views.showlist, name='showlist'),
    path('movies/edit/<int:pk>/', views.movie_edit, name='movie_edit'),
    path('movies/delete/<int:pk>/', views.movie_delete, name='movie_delete'),
]