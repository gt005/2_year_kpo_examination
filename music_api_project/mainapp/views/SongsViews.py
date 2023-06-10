from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import SongModel
from ..serializers import SongSerializer, SongDetailSerializer


class SongList(ListAPIView):
    queryset = SongModel.objects.all()
    serializer_class = SongSerializer


class SongDetail(RetrieveAPIView):
    queryset = SongModel.objects.all()
    serializer_class = SongDetailSerializer
    lookup_field = 'id'
