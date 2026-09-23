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
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return SocialLink.objects.all()
        return SocialLink.objects.filter(is_active=True)


class FooterMenuViewSet(viewsets.ModelViewSet):
    serializer_class = FooterMenuSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return FooterMenu.objects.all()
        return FooterMenu.objects.filter(is_active=True)