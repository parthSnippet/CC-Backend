from django.db import models


class ContactLead(models.Model):

    PROJECT_TYPE_CHOICES = [
        ("web_development", "Web Development"),
        ("software_development", "Software Development"),
        ("automation", "Automation"),
        ("ai_platforms", "AI Platforms"),
        ("erp_crm", "ERP & CRM"),
        ("it_solutions", "IT Solutions"),
        ("book_a_call", "Book a Call"),
        ("not_sure", "Not sure yet"),
    ]

    BUDGET_CHOICES = [
        ("under_1k", "Under $1k"),
        ("1k_5k", "$1k - $5k"),
        ("5k_15k", "$5k - $15k"),
        ("15k_30k", "$15k - $30k"),
        ("30k_plus", "$30k+"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("in_progress", "In Progress"),
        ("converted", "Converted"),
        ("closed", "Closed"),
    ]

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    company = models.CharField(
        max_length=200,
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPE_CHOICES,
        blank=True

    )

    budget = models.CharField(
        max_length=30,
        choices=BUDGET_CHOICES,
        blank=True
    )

    timeline = models.CharField(
        max_length=100,
        blank=True
    )

    project_brief = models.TextField()

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