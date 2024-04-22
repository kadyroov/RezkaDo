from django.db import models

class Movie(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название фильма',  # Человеко-понятное название для поля
        help_text='Введите название фильма, до 250 символов'  # Дополнительное пояснение
    )
    year = models.CharField(
        max_length=4,  # Дополнительно, добавил ограничение по количеству символов
        verbose_name='Год выпуска',  # Название для года выпуска
        help_text='Введите год, когда фильм был выпущен'  # Инструкция по заполнению
    )
    country = models.CharField(
        max_length=100,  # Дополнительно, добавил ограничение по количеству символов
        verbose_name='Страна производства',  # Название для поля страны
        help_text='Укажите страну, где был произведен фильм'  # Инструкция по заполнению
    )
    genre = models.CharField(
        max_length=100,  # Также можно ограничить количество символов
        verbose_name='Жанр фильма',  # Название для поля жанра
        help_text='Введите жанр фильма, например: драма, комедия, экшн'  # Дополнительная подсказка
    )
    url = models.URLField(
        verbose_name='Ссылка на информацию о фильме',  # Название для поля URL
        help_text='Введите полный URL-адрес с информацией о фильме'  # Инструкция по заполнению
    )
    img = models.URLField(
        verbose_name='Ссылка на изображение',  # Название для поля изображения
        help_text='Введите URL-адрес изображения или постера фильма'  # Инструкция по заполнению
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',  # Название для поля даты создания
        help_text='Дата, когда запись была создана. Устанавливается автоматически.'
    )

    def __str__(self):
        return f"{self.title} - {self.year}"  # Исправлено использование поля

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-created_at']  # Сортировка по дате создания, по убыванию
