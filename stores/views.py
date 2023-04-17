from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OpeningHoursSerializer, StoreSerializer
from .models import Store, OpeningHours


class StoreListCreate(ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class TimesListCreate(ListCreateAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.all()


class StoreDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class TimesDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.all()
