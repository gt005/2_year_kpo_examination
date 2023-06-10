from django.contrib import admin
from .models import SongModel, PlaylistModel

admin.site.register(SongModel)
admin.site.register(PlaylistModel)