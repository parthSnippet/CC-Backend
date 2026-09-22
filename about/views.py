from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly
from .models import AboutPage
from .serializers import AboutPageSerializer


class AboutPageViewSet(viewsets.ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [IsAdminOrReadOnly]