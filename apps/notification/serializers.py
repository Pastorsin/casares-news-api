from push_notifications.models import WebPushDevice
from rest_framework.serializers import ModelSerializer


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = WebPushDevice
        fields = ["registration_id", "p256dh", "auth", "browser"]
