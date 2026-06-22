from django.db import models
from core.models import SoftDeleteModel, AuditMixin


class CounsellingSession(SoftDeleteModel, AuditMixin):
    """Sensitive: Counselling session. Restrict to IsCounsellor."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="counselling_sessions",
        db_index=True,
    )
    counsellor = models.ForeignKey(
        "people.TeacherProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conducted_sessions",
        db_index=True,
    )
    session_date = models.DateField()
    presenting_issue = models.TextField()
    notes = models.TextField(blank=True, default="")
    follow_up_date = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["-session_date"]
        verbose_name = "Counselling Session"
        verbose_name_plural = "Counselling Sessions"
    def __str__(self):
        return f"{self.student} - {self.session_date}"