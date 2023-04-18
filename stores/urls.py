from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserList.as_view()),
    path("users/create/", views.UserCreate.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("stores/", views.StoreListCreate.as_view()),
    path("stores/<int:pk>/", views.StoreDetail.as_view()),
    path("times/", views.TimesListCreate.as_view()),
    path("times/<int:pk>/", views.TimesDetail.as_view()),
]
