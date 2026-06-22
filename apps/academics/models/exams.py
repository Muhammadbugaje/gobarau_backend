from django.db import models
from core.models import BaseModel

class ExamRegistration(BaseModel):
    """Student's registration for an exam subject."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="exam_registrations",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="exam_registrations",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="exam_registrations",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="exam_registrations",
        db_index=True,
    )
    is_registered = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ["student", "subject"]
        verbose_name = "Exam Registration"
        verbose_name_plural = "Exam Registrations"
        unique_together = ("student", "subject", "term")

    def __str__(self):
        return f"{self.student} - {self.subject} Registration"

class ExamResult(BaseModel):
    """Final exam result for a student in a subject."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="exam_results",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="exam_results",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="exam_results",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="exam_results",
        db_index=True,
    )
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5, blank=True, default="")
    remark = models.CharField(max_length=200, blank=True, default="")

    class Meta:
        ordering = ["-score"]
        verbose_name = "Exam Result"
        verbose_name_plural = "Exam Results"
        unique_together = ("student", "subject", "term")

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.score}"