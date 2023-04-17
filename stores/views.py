from rest_framework.generics import ListCreateAPIView
from .serializers import OpeningHoursSerializer, StoreSerializer
from .models import Store, OpeningHours


class StoreListCreate(ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class TimesListCreate(ListCreateAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.all()
