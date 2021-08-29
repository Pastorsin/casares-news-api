from django.urls import path

from news.views import ArticleView

urlpatterns = [
    path("", ArticleView.as_view()),
]
