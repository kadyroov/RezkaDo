# Generated by Django 5.0.4 on 2024-04-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_movie_country_alter_movie_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(help_text='Введите год, когда фильм был выпущен', max_length=4, verbose_name='Год выпуска'),
        ),
    ]
