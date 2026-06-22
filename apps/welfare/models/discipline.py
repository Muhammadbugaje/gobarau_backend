from django.db import models
from core.models import SoftDeleteModel, AuditMixin
from core.choices import DisciplinaryStatusChoices, MeritDirectionChoices


class DisciplinaryRecord(SoftDeleteModel, AuditMixin):
    """Disciplinary record. Admin level only."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="disciplinary_records",
        db_index=True,
    )
    incident_date = models.DateField()
    incident_type = models.CharField(max_length=100)
    description = models.TextField()
    action_taken = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=DisciplinaryStatusChoices.choices,
        default=DisciplinaryStatusChoices.PENDING,
        db_index=True,
    )
    class Meta:
        ordering = ["-incident_date"]
        verbose_name = "Disciplinary Record"
        verbose_name_plural = "Disciplinary Records"
    def __str__(self):
        return f"{self.student} - {self.incident_type} ({self.incident_date})"

class MeritDeduction(SoftDeleteModel, AuditMixin):
    """Merit/Demerit point tracking."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="merit_deductions",
        db_index=True,
    )
    points = models.PositiveIntegerField(default=1)
    direction = models.CharField(
        max_length=10,
        choices=MeritDirectionChoices.choices,
        default=MeritDirectionChoices.ADD,
        db_index=True,
    )
    reason = models.CharField(max_length=200)
    recorded_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recorded_merits",
        db_index=True,
    )
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Merit/Deduction"
        verbose_name_plural = "Merits/Deductions"
    def __str__(self):
        return f"{self.student} - {self.direction} {self.points} points"