from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import ContactLead
from .serializers import ContactLeadSerializer


class ContactLeadCreateView(generics.ListCreateAPIView):
    queryset = ContactLead.objects.all().order_by("-created_at")
    serializer_class = ContactLeadSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAdminUser()]
        return [AllowAny()]


class ContactLeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactLead.objects.all()
    serializer_class = ContactLeadSerializer
    permission_classes = [IsAdminUser]