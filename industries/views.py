from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from core.permissions import IsAdminOrReadOnly

from .models import Industry
from .serializers import IndustrySerializer


class IndustryViewSet(viewsets.ModelViewSet):
    serializer_class = IndustrySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Industry.objects.all()
        return Industry.objects.filter(is_active=True)

    def get_object(self):
        lookup = self.kwargs.get("pk")
        queryset = self.get_queryset()

        if lookup and lookup.isdigit():
            obj = queryset.filter(pk=lookup).first()
        else:
            obj = queryset.filter(slug=lookup).first()

        if not obj:
            raise NotFound("No Industry matches the given query.")

        self.check_object_permissions(self.request, obj)
        return obj