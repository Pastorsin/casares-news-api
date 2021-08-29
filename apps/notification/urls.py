from rest_framework.routers import DefaultRouter

from notification.views import NotificationViewSet

router = DefaultRouter()
router.register("", NotificationViewSet, basename="notification")
urlpatterns = router.urls
