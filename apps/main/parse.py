import requests
from bs4 import BeautifulSoup


from apps.main.core import token
import json

# from models import Movie
from rest_framework.response import Response

def get_films(URL, HEADERS):
        response = requests.get(token.URL, headers=token.HEADERS)
        html = response.text
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
            # if Movie.objects.filter(title=title, year=year).exists():
            #     continue
            # else:
            if year and country and genre:
                data.append({
                'title': title,
                'year': year,
                'country': country,
                'genre': genre,
                'url': url,
                'img': img
                })

            with open('result1.json', 'w') as file:
                json.dump(data, file, indent = 4, ensure_ascii = False)

        return Response(data)

print(get_films(token.URL, token.HEADERS))


# def get_films(URL, HEADERS):
#     response = requests.get(token.URL, headers=token.HEADERS)
#     html = response.text
#     soap = BeautifulSoup(html, 'lxml').find(
#     'div', {'class': 'b-content__inline_items'}
#     ).find_all(
#     'div', {'class' : 'b-content__inline_item'}
#     )
    
#     data = []
#     for item in soap:
#         base = item.find('div', {'class':"b-content__inline_item-link"})
#         pic = item.find('div', {'class': "b-content__inline_item-cover"})
#         url = base.find('a').get('href')
#         img = pic.find('a').find('img').get('src')
#         title = base.find('a').text
#         info = base.find('div').text
#         year, country, genre   = info.split(", ")
#         if Movie.objects.filter(title=title, year=year).exists():
#             continue
        
    
#         data.append({
#         'title': title,
#         'year': year,
#         'country': country,
#         'genre': genre,
#         'url': url,
#         'img': img
#         })

#     with open('result1.json', 'w') as file:
#         json.dump(data, file, indent = 4, ensure_ascii = False)

#     return Response(data)
    


# # get_films(HEAD.URL,HEAD.HEADERS)