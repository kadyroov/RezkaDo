from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    country = models.TextField()
    genre = models.TextField()
    url = models.TextField()
    img = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
        )


    def __str__(self):
        return f"{self.name} - {self.year}" 
    
    def movie_exists(self):
        return Movie.objects.filter(title=self.title, year=self.year).exists()
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-created_at']