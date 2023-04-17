from django.urls import path
from . import views

urlpatterns = [
    path("stores/", views.StoreListCreate.as_view()),
    #     path("stores/<int:pk>/", views.StoreDetail.as_view()),
    #     path("stores/create/", views.StoreCreate.as_view()),
    path("times/", views.TimesListCreate.as_view()),
]
