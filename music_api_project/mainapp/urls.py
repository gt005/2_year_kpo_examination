from django.urls import path
from .views import SongList, SongDetail


urlpatterns = [
    path('songs/', SongList.as_view(), name='songs_list'),
    path('songs/<int:id>/', SongDetail.as_view(), name='song_detail'),
]