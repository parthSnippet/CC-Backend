from django.db import models


class ComradeAIQuery(models.Model):
    query = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Comrade AI Query"
        verbose_name_plural = "Comrade AI Queries"

    def __str__(self):
        return self.query[:80]