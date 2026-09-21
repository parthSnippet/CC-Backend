from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly

from .models import BlogCategory, BlogPost
from .serializers import BlogCategorySerializer, BlogPostSerializer


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.filter(is_active=True)
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = (
        BlogPost.objects
        .filter(is_published=True)
        .select_related("category")
    )

    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminOrReadOnly]