from rest_framework import serializers

from ..models import PlaylistModel
from .SongsSerializers import SongSerializer


class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = PlaylistModel
        fields = ['id', 'name', 'songs']
