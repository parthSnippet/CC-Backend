from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly

from .models import BlogCategory, BlogPost
from .serializers import BlogCategorySerializer, BlogPostSerializer


class BlogCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return BlogCategory.objects.all()
        return BlogCategory.objects.filter(is_active=True)


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = BlogPost.objects.select_related("category")
        if self.request.user and self.request.user.is_staff:
            return qs.all()
        return qs.filter(is_published=True)