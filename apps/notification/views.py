import logging

from push_notifications.models import WebPushDevice
from rest_framework import viewsets

from notification.serializers import NotificationSerializer

logger = logging.getLogger(__name__)


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = WebPushDevice.objects.all()
    serializer_class = NotificationSerializer

    authentication_classes = []
    permission_classes = []

    http_method_names = ["post"]
