from rest_framework.views import APIView
from rest_framework.response import Response

from apps.main.models import Movie
from apps.api.serializers import MovieSerializer
from apps.main.parse import get_films

from bs4 import BeautifulSoup
import requests
import json
from apps.main.core import token

class MovieListView(APIView):
    # serializer_class = MovieSerializer
    # queryset = Movie.objects.all()
    
    def get_films(URL, HEADERS):
        response = requests.get(token.URL, headers=token.HEADERS)
        html = response.text
        soap = BeautifulSoup(html, 'lxml').find(
        'div', {'class': 'b-content__inline_items'}
    ).find_all(
        'div', {'class': 'b-content__inline_item'}
    )
    
        for item in soap:
            base = item.find('div', {'class': "b-content__inline_item-link"})
            pic = item.find('div', {'class': "b-content__inline_item-cover"})
            url = base.find('a').get('href')
            img = pic.find('a').find('img').get('src')
            title = base.find('a').text
            info = base.find('div').text

            info_parts = info.split(", ")
        
            if len(info_parts) >= 3:
                year, country, genre = info_parts[:3]  
            else:
                continue
        
        
            movie, created = Movie.objects.get_or_create(
            title=title,
            defaults={
                'year': year,
                'country': country,
                'genre': genre,
                'url': url,
                'img': img
            }
        )

        return Response({'message': 'Data added successfully'})


    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    

    
        