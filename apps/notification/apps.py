from django.apps import AppConfig


class NotificationConfig(AppConfig):
    name = "notification"

    def ready(self):
        # Init signals
        from notification import signals
