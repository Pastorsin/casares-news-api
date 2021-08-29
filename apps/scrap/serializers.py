import logging

from news.models import Article, Newspaper

logger = logging.getLogger(__name__)


class NewspaperSerializer:
    def __init__(self, newspaper):
        self.newspaper = newspaper

    def serialize(self):
        return {"name": self.newspaper.name(), "url": self.newspaper.url()}

    def save(self):
        serialized_newspaper = self.newspaper.serialize()
        newspaper, _ = Newspaper.objects.get_or_create(**serialized_newspaper)

        return newspaper


class ArticleSerializer:
    def __init__(self, article):
        self.newspaper_serializer = NewspaperSerializer(article.source())
        self.article = article

    def serialize_id(self, source):
        return {
            "title": self.article.title(),
            "url": self.article.url(),
            "source": source,
        }

    def serialize_defaults(self):
        return {
            "photo": self.article.photo(),
            "description": self.article.description(),
            "date": self.article.date(),
        }

    def save(self):
        source = self.newspaper_serializer.save()

        new_article, created = Article.objects.get_or_create(
            **self.serialize_id(source),
            defaults=self.serialize_defaults(),
        )

        if created:
            logger.info(f"Article created: '{new_article}'")
            return new_article
        else:
            logger.error(
                f"'{self.article}' already exists: 'PK={new_article.pk}'"
            )
            return None
