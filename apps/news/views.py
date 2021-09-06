from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from rdf_io.views import to_rdfbyid

from news.models import Article, Newspaper
from news.parsers import ParseException, parse_args
from news.renderers import error_response, rdf_response
from news.serializers import serialize_to_rdf


class ArticleView(View):
    # Accepts the follows MIME:
    # https://rdflib.readthedocs.io/en/stable/plugin_parsers.html
    DEFAULT_MIME_FORMAT = "text/turtle"

    def get(self, request):
        try:
            args = parse_args(request.GET)
        except ParseException as e:
            return error_response(e)
        else:
            instances = serialize_to_rdf(Article, *args)

            return rdf_response(
                instances,
                mime_format=request.content_type,
                mime_default=self.DEFAULT_MIME_FORMAT,
            )

class ArticleDetailView(View):
    def get(self, request, id):
        return to_rdfbyid(request, "article", id)

class NewspaperDetailView(View):
    def get(self, request, name):
        try:
            uncoded_name = name.replace("_", " ")
            newspaper = Newspaper.objects.get(name__iexact=uncoded_name)
            newspaper_id = newspaper.id
        except ObjectDoesNotExist:
            newspaper_id = -1

        return to_rdfbyid(request, "newspaper", newspaper_id)
