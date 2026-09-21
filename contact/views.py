from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import ContactLead
from .serializers import ContactLeadSerializer


class ContactLeadCreateView(generics.CreateAPIView):
    queryset = ContactLead.objects.all()
    serializer_class = ContactLeadSerializer
    permission_classes = [AllowAny]