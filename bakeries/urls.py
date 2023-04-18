from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # authentication django token
    path("django-token/", obtain_auth_token, name="api_token_auth"),
    # API routes
    path("api/v1/", include("stores.urls")),
]
