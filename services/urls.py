from rest_framework.routers import DefaultRouter

from .views import ServiceVideoViewSet, ServiceViewSet


router = DefaultRouter()

router.register(
    r"services",
    ServiceViewSet,
    basename="service",
)

router.register(
    r"service-videos",
    ServiceVideoViewSet,
    basename="service-video",
)

urlpatterns = router.urls