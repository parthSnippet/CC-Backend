from rest_framework import generics

from .models import ComradeAIQuery
from .permissions import IsAdminForReadOnly
from .serializers import ComradeAIQuerySerializer


class ComradeAIQueryListCreateView(generics.ListCreateAPIView):
    queryset = ComradeAIQuery.objects.all()
    serializer_class = ComradeAIQuerySerializer
    permission_classes = [IsAdminForReadOnly]