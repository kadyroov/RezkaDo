from django.urls import path

from apps.api.views import MovieListView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
]