from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'genre', 'url', 'img', 'created_at']
    list_filter = ['year']
    search_fields = ['title']
    readonly_fields = ['created_at']