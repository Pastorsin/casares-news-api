from django.urls import path

from news.views import ArticleView, ArticleDetailView, NewspaperDetailView

urlpatterns = [
    path("articles/", ArticleView.as_view()),
    path("articles/<int:id>/", ArticleDetailView.as_view()),
    path("newspapers/<str:name>/", NewspaperDetailView.as_view()),
]
