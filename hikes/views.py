from .models import Hike
from .serializers import HikeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class HikeList(ListCreateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer


class HikeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
