from django.db import models
from core.models import BaseModel

class CAConfiguration(BaseModel):
    """Continuous Assessment configuration for a subject and class level."""
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="ca_configurations",
        db_index=True,
    )
    class_level = models.ForeignKey(
        "administration.ClassLevel",
        on_delete=models.CASCADE,
        related_name="ca_configurations",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="ca_configurations",
        db_index=True,
    )
    ca_weight = models.DecimalField(max_digits=5, decimal_places=2)
    exam_weight = models.DecimalField(max_digits=5, decimal_places=2)
    total_weight = models.DecimalField(max_digits=5, decimal_places=2, default=100)

    class Meta:
        ordering = ["subject", "class_level"]
        verbose_name = "CA Configuration"
        verbose_name_plural = "CA Configurations"
        unique_together = ("subject", "class_level", "term")

    def __str__(self):
        return f"{self.subject} - {self.class_level} CA Config"