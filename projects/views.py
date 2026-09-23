from rest_framework import viewsets
from django.db.models import Prefetch

from core.permissions import IsAdminOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = Project.objects.prefetch_related("services", "industries", "technologies")
        if self.request.user and self.request.user.is_staff:
            return qs.all()
        return qs.filter(is_active=True)