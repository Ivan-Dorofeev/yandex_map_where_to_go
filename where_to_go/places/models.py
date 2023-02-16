from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField('Название места', max_length=50)
    long_description = models.CharField('Короткое описание', max_length=500)
    short_description = HTMLField('Полное описание')
    latitude = models.FloatField('Широта')
    longtitude = models.FloatField('Долгота')

    class Meta:
        ordering = ["title", ]

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, verbose_name='Локация', related_name='images', on_delete=models.CASCADE, )
    image = models.ImageField(verbose_name='Картинка')
    index = models.IntegerField(verbose_name='Позиция', null=True, blank=True)

    def __str__(self):
        return f'{self.location} - {self.image}'

    class Meta:
        ordering = ["location", ]
