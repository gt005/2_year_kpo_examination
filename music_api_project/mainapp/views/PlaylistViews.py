from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import PlaylistModel, SongModel
from ..serializers import PlaylistSerializer


class PlaylistCreate(CreateAPIView):
    queryset = PlaylistModel.objects.all()
    serializer_class = PlaylistSerializer

    def create(self, request, *args, **kwargs):
        if PlaylistModel.objects.filter(name=request.data.get('name')).exists():
            return Response(
                {"message": "Плейлист с таким названием существует."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)


class PlaylistAddSong(APIView):
    def post(self, request, *args, **kwargs):
        song_id = request.data.get('song_id')
        playlist_id = kwargs.get('playlist_id')

        print(song_id, playlist_id)

        if not song_id or not playlist_id:
            return Response(
                {"message": "Необходимо указать song_id и playlist_id."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not SongModel.objects.filter(pk=song_id).exists():
            return Response(
                {"message": "Такой песни не существует."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not PlaylistModel.objects.filter(pk=playlist_id).exists():
            return Response(
                {"message": "Такого плейлиста не существует."},
                status=status.HTTP_400_BAD_REQUEST
            )

        playlist = PlaylistModel.objects.get(pk=playlist_id)
        song = SongModel.objects.get(pk=song_id)
        playlist.songs.add(song)
        playlist.save()

        return Response({"message": 'ok'}, status=status.HTTP_200_OK)