from django.urls import path

from .views import ContactLeadCreateView, ContactLeadDetailView


urlpatterns = [
    path(
        "contact/",
        ContactLeadCreateView.as_view(),
        name="contact-create",
    ),
    path(
        "contact/<int:pk>/",
        ContactLeadDetailView.as_view(),
        name="contact-detail",
    ),
]