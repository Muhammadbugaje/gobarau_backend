from django.db import models
from core.models import BaseModel

class Class(BaseModel):
    """Represents a specific class instance (e.g., JSS 1A) for a session."""
    name = models.CharField(max_length=100)
    class_level = models.ForeignKey(
        "administration.ClassLevel",
        on_delete=models.CASCADE,
        related_name="classes",
        db_index=True,
    )
    wing = models.ForeignKey(
        "administration.Wing",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="classes",
        db_index=True,
    )
    campus = models.ForeignKey(
        "administration.Campus",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="classes",
        db_index=True,
    )
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="classes",
        db_index=True,
    )
    capacity = models.PositiveIntegerField(default=40)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return f"{self.name} ({self.session.name})"