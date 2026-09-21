from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly

from .models import SiteSetting, SocialLink, FooterMenu
from .serializers import (
    SiteSettingSerializer,
    SocialLinkSerializer,
    FooterMenuSerializer,
)


class SiteSettingViewSet(viewsets.ModelViewSet):
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer
    permission_classes = [IsAdminOrReadOnly]


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.filter(is_active=True)
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAdminOrReadOnly]


class FooterMenuViewSet(viewsets.ModelViewSet):
    queryset = FooterMenu.objects.filter(is_active=True)
    serializer_class = FooterMenuSerializer
    permission_classes = [IsAdminOrReadOnly]