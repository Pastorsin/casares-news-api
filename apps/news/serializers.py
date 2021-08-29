from django.contrib.contenttypes.models import ContentType

from rdf_io.models import ObjectMapping
from rdf_io.views import build_rdf
from rdflib import Graph


def serialize_to_rdf(Model, start=0, offset=None):
    content_type = ContentType.objects.get(model=Model.__name__.lower())
    obj_mapping_list = ObjectMapping.objects.filter(content_type=content_type)

    graph = Graph()

    if offset is None:
        objects = Model.objects.all()[start:]
    else:
        end = start + offset
        objects = Model.objects.all()[start:end]

    for object in objects:
        build_rdf(graph, object, obj_mapping_list, includemembers=True)

    return graph
