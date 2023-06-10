from rest_framework import serializers

from ..models import SongModel


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ['id', 'name', 'author', 'genre']


class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ['name', 'duration_seconds', 'author', 'genre', 'album_name']
