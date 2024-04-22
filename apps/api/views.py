from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.main.models import Movie
from apps.api.serializers import MovieSerializer


from apps.main.parse import main

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny()]

        
        return [permissions.IsAdminUser()]
    
    def get(self, request, *args, **kwargs):
        main()
        return super().get(request, *args, **kwargs)



class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny()]


        return [permissions.IsAdminUser()]

    
        