from rest_framework.routers import DefaultRouter

from .views import AboutPageViewSet


router = DefaultRouter()

router.register(
    r"about",
    AboutPageViewSet,
    basename="about",
)

urlpatterns = router.urls