from django.db import models


class Newspaper(models.Model):

    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name

    @property
    def encoded_name(self):
        return self.name.lower().replace(" ", "_")


class Article(models.Model):

    title = models.CharField(max_length=255)
    url = models.URLField()
    photo = models.URLField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    source = models.ForeignKey(Newspaper, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["title", "date", "source"]
        ordering = ["-date"]

    def __str__(self):
        pretty_date = self.date.strftime("[%m/%d/%Y-%H:%M:%S]")

        return f"{pretty_date} {self.title} - {self.source}"

    @property
    def formated_date(self):
        return self.date.isoformat()
