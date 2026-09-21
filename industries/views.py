from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly

from .models import Industry
from .serializers import IndustrySerializer


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.filter(is_active=True)
    serializer_class = IndustrySerializer
    permission_classes = [IsAdminOrReadOnly]