from django.urls import path

from apps.api.views import MovieListCreate, MovieRetrieveUpdateDestroy


urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie_list'),

    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
]