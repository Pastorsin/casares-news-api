from django.views import View

from news.models import Article
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
