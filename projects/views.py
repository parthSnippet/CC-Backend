from rest_framework import viewsets
from django.db.models import Prefetch

from core.permissions import IsAdminOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(
        is_active=True
    ).prefetch_related(
        "services",
        "industries",
        "technologies",
    )
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]