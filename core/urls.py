from rest_framework.routers import DefaultRouter

from .views import (
    SiteSettingViewSet,
    SocialLinkViewSet,
    FooterMenuViewSet,
)


router = DefaultRouter()

router.register(
    r"settings",
    SiteSettingViewSet,
    basename="site-setting",
)

router.register(
    r"social-links",
    SocialLinkViewSet,
    basename="social-link",
)

router.register(
    r"footer-menus",
    FooterMenuViewSet,
    basename="footer-menu",
)

urlpatterns = router.urls