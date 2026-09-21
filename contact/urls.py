from django.urls import path

from .views import ContactLeadCreateView


urlpatterns = [
    path(
        "contact/",
        ContactLeadCreateView.as_view(),
        name="contact-create",
    ),
]