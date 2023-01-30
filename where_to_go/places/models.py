from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField('Название места', max_length=50)
    description = models.CharField('Короткое описание', max_length=500, blank=True, null=True)
    text = HTMLField('Полное описание',blank=True, null=True)
    latitude = models.FloatField('Широта', blank=True, null=True)
    longtitude = models.FloatField('Долгота', blank=True, null=True)


    class Meta:
        ordering = ["title", ]

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, verbose_name='Локация', related_name='images', on_delete=models.CASCADE,
                                 blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.location} - {self.image}'

    class Meta:
        ordering = ["location", ]
