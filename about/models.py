from django.db import models


class AboutPage(models.Model):
    # About Us Stats
    projects_delivered = models.CharField(
        max_length=20,
        default="50+"
    )
    happy_clients = models.CharField(
        max_length=20,
        default="30+"
    )
    years_experience = models.CharField(
        max_length=20,
        default="3+"
    )
    tech_experts = models.CharField(
        max_length=20,
        default="10+"
    )

    # How We Work
    how_we_work_title = models.CharField(
        max_length=200,
        default="How we work"
    )

    how_we_work_description = models.TextField(
        default="Our process is built around clarity, speed and accountability."
    )

    how_we_work_points = models.JSONField(
        default=list,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return "About Us"