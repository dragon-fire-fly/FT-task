from rest_framework import filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import (
    OpeningHoursSerializer,
    StoreSerializer,
    UserSerializer,
    UserCreateSerializer,
)
from .models import Store, OpeningHours


class UserCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class StoreListCreate(ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ["store_name", "store_address"]


class TimesListCreate(ListCreateAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.all()


class StoreDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class TimesDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.all()
