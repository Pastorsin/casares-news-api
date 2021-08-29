import json
import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import Article
from push_notifications.models import WebPushDevice

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Article)
def notify(sender, instance, **kwargs):
    notification = json.dumps({"title": instance.title, "url": instance.url})

    for webpush in WebPushDevice.objects.all():
        try:
            webpush.send_message(notification)
        except Exception as e:
            logger.error(e, exc_info=True)
            continue
