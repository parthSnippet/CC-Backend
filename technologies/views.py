from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly

from .models import Technology
from .serializers import TechnologySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.filter(is_active=True)
    serializer_class = TechnologySerializer
    permission_classes = [IsAdminOrReadOnly]