from django.urls import path
from .views import SongList, SongDetail, PlaylistCreate, PlaylistAddSong


urlpatterns = [
    path('songs/', SongList.as_view(), name='songs_list'),
    path('songs/<int:id>/', SongDetail.as_view(), name='song_detail'),
    path('playlists/', PlaylistCreate.as_view(), name='playlist_create'),
    path('playlists/<int:playlist_id>/songs/', PlaylistAddSong.as_view(), name='playlist_add_song'),
]