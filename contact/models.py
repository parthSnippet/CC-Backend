from django.db import models


class ContactLead(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("in_progress", "In Progress"),
        ("converted", "Converted"),
        ("closed", "Closed"),
    ]

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    company = models.CharField(
        max_length=200,
        blank=True
    )

    subject = models.CharField(
        max_length=250,
        blank=True
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"