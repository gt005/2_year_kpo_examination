from django.db import models
from .SongModel import SongModel


class PlaylistModel(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(SongModel)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'