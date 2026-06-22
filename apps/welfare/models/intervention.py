from django.db import models
from core.models import SoftDeleteModel, AuditMixin
from core.choices import InterventionStatusChoices

class InterventionCase(SoftDeleteModel, AuditMixin):
    """Intervention case. Admin level only."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="intervention_cases",
        db_index=True,
    )
    case_type = models.CharField(max_length=100)
    description = models.TextField()
    opened_at = models.DateField(auto_now_add=True)
    closed_at = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=InterventionStatusChoices.choices,
        default=InterventionStatusChoices.OPEN,
        db_index=True,
    )
    class Meta:
        ordering = ["-opened_at"]
        verbose_name = "Intervention Case"
        verbose_name_plural = "Intervention Cases"
    def __str__(self):
        return f"Case {self.public_id} - {self.student}"

class InterventionNote(SoftDeleteModel, AuditMixin):
    """Progress note on an intervention case."""
    case = models.ForeignKey(
        "welfare.InterventionCase",
        on_delete=models.CASCADE,
        related_name="notes",
        db_index=True,
    )
    note = models.TextField()
    added_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="intervention_notes",
        db_index=True,
    )
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-added_at"]
        verbose_name = "Intervention Note"
        verbose_name_plural = "Intervention Notes"
    def __str__(self):
        return f"Note on {self.case} by {self.added_by}"

class Absence(SoftDeleteModel, AuditMixin):
    """Extended student absence record."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="absences",
        db_index=True,
    )
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    is_excused = models.BooleanField(default=False, db_index=True)
    parent_notified = models.BooleanField(default=False)
    class Meta:
        ordering = ["-from_date"]
        verbose_name = "Absence"
        verbose_name_plural = "Absences"
    def __str__(self):
        return f"{self.student} absent from {self.from_date} to {self.to_date}"


class WelfareReport(SoftDeleteModel, AuditMixin):
    """Periodic welfare summary report."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="welfare_reports",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="welfare_reports",
        db_index=True,
    )
    overall_welfare_level = models.CharField(max_length=50)
    recommendations = models.TextField(blank=True, default="")
    prepared_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prepared_welfare_reports",
        db_index=True,
    )
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Welfare Report"
        verbose_name_plural = "Welfare Reports"
    def __str__(self):
        return f"Welfare Report for {self.student} - {self.term}"