# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 다른 URL 패턴들...
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("playlist/", include("playlist.urls")),
]
