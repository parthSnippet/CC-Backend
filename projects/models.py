from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    short_description = models.CharField(max_length=300)
    description = models.TextField()

    client_name = models.CharField(
        max_length=200,
        blank=True
    )

    project_url = models.URLField(
        blank=True
    )

    featured_image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    services = models.ManyToManyField(
        "services.Service",
        blank=True,
        related_name="projects"
    )

    industries = models.ManyToManyField(
        "industries.Industry",
        blank=True,
        related_name="projects"
    )

    technologies = models.ManyToManyField(
        "technologies.Technology",
        blank=True,
        related_name="projects"
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title