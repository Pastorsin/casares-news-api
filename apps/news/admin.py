from django.contrib import admin

from news.models import Article, Newspaper

admin.site.register(Article)
admin.site.register(Newspaper)
