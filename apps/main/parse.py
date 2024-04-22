import requests
from bs4 import BeautifulSoup
from apps.main.models import Movie
from django.conf import settings

import json

# from models import Movie
from rest_framework.response import Response

def get_hmtl(URL, HEADERS):
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
         return None
    
    return response.text
         


def processing(html):
        soap = BeautifulSoup(html, 'lxml').find(
        'div', {'class': 'b-content__inline_items'}
        ).find_all(
        'div', {'class' : 'b-content__inline_item'}
        )
    
        data = []
        for item in soap:
            base = item.find('div', {'class':"b-content__inline_item-link"})
            pic = item.find('div', {'class': "b-content__inline_item-cover"})
            url = base.find('a').get('href')
            img = pic.find('a').find('img').get('src')
            title = base.find('a').text
            info = base.find('div').text
            info_parts = info.split(", ")

            if len(info_parts) >= 3:
                year, country, genre   = info.split(", ")
            else:
                year = country = genre = None
            
            if year and country and genre:
                data.append({
                'title': title,
                'year': year,
                'country': country,
                'genre': genre,
                'url': url,
                'img': img
                })

        return data

def main():
    URL = settings.URL
    HEADERS = settings.HEADERS
    html = get_hmtl(URL, HEADERS)
    if html is None:
        return None
    
    data = processing(html)

    for item in data:
        movie, created = Movie.objects.get_or_create(title=item['title'])         
        
        if created:
            movie.title = item['title']
            movie.year = item['year'] if item['year'] else None
            movie.country = item['country']
            movie.genre = item['genre']
            movie.url = item['url']
            movie.img = item['img']
            movie.save()

    return True


