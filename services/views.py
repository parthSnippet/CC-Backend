from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from core.permissions import IsAdminOrReadOnly

from .models import Service, ServiceVideo
from .serializers import ServiceSerializer, ServiceVideoSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Service.objects.all()

        return Service.objects.filter(is_active=True)

    def get_object(self):
        lookup = self.kwargs.get("pk")
        queryset = self.get_queryset()

        # Admin actions (update/delete) use numeric id
        if lookup and lookup.isdigit():
            obj = queryset.filter(pk=lookup).first()
        else:
            obj = queryset.filter(slug=lookup).first()

        if not obj:
            raise NotFound("No Service matches the given query.")

        self.check_object_permissions(self.request, obj)

        return obj


class ServiceVideoViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceVideoSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = ServiceVideo.objects.select_related("service")

        if self.request.user and self.request.user.is_staff:
            return queryset

        return queryset.filter(
            is_active=True,
            service__is_active=True,
        )