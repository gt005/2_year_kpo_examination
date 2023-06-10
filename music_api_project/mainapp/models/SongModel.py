from django.db import models


class SongModel(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'