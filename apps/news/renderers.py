from django.http import HttpResponse

from rdf_io.models import Namespace
from rdflib.plugin import PluginException


def rdf_response(graph, mime_format, mime_default, encoding="utf-8"):
    try:
        content = graph.serialize(
            format=mime_format, context=_get_rdf_context()
        )
    except PluginException:
        content = graph.serialize(
            format=mime_default, context=_get_rdf_context()
        )

    return HttpResponse(
        content,
        content_type=f"{mime_format}; charset={encoding}",
    )


def _get_rdf_context():
    namespaces = Namespace.objects.all()
    return {n.prefix: n.uri for n in namespaces}


def error_response(error_msg):
    return HttpResponse(content=f" Error - {error_msg}", status=501)
