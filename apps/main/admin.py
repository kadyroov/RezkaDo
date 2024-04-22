from django.contrib import admin
from apps.main.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Основная информация", {  # Заголовок секции
            "fields": ("title", "year", "country", "genre"),  # Какие поля включить
        }),
        ("Дополнительные сведения", {
            "fields": ("url", "img"),  # Поля с дополнительной информацией
        }),
        ("Служебная информация", {
            "fields": ("created_at",),  # Поле даты создания
            "classes": ("collapse",),  # Дополнительно, делаем секцию сворачиваемой
        }),
    )

    list_display = ("title", "year", "country", "genre", "created_at")
    search_fields = ("title", "year", "country", "genre")
    list_filter = ("country", "genre", "year")
    ordering = ["-created_at"]
