from django.urls import path, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

DJANGO_URLS = [
    path("admin/", admin.site.urls),
]

if settings.ONLY_DJANGO_APPS:
    OWN_URLS = []
else:
    OWN_URLS = [
        path("articles/", include("news.urls")),
        path("notification/", include("notification.urls")),
    ]

urlpatterns = DJANGO_URLS + OWN_URLS
