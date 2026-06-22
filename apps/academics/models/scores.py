from django.db import models
from core.models import BaseModel

class Score(BaseModel):
    """Student's score for a subject in a term."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="scores",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="scores",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="scores",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="scores",
        db_index=True,
    )
    ca_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grade = models.CharField(max_length=5, blank=True, default="")
    grade_point = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    is_locked = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-total_score"]
        verbose_name = "Score"
        verbose_name_plural = "Scores"
        unique_together = ("student", "subject", "term")

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.total_score}"

class ReportCard(BaseModel):
    """Termly report card for a student."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="report_cards",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="report_cards",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="report_cards",
        db_index=True,
    )
    total_score = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    position = models.PositiveIntegerField(null=True, blank=True)
    is_published = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-average"]
        verbose_name = "Report Card"
        verbose_name_plural = "Report Cards"
        unique_together = ("student", "term", "class_assigned")

    def __str__(self):
        return f"{self.student} - {self.term} Report Card"

class Assignment(BaseModel):
    """Assignment given to a class for a subject."""
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="assignments",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="assignments",
        db_index=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    due_date = models.DateField()
    max_score = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    is_published = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-due_date"]
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    def __str__(self):
        return f"{self.title} - {self.class_assigned}"

class AssignmentSubmission(BaseModel):
    """Student's submission for an assignment."""
    assignment = models.ForeignKey(
        "academics.Assignment",
        on_delete=models.CASCADE,
        related_name="submissions",
        db_index=True,
    )
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="assignment_submissions",
        db_index=True,
    )
    submission_date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(blank=True, default="")
    is_late = models.BooleanField(default=False)
    is_graded = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submission_date"]
        verbose_name = "Assignment Submission"
        verbose_name_plural = "Assignment Submissions"
        unique_together = ("assignment", "student")

    def __str__(self):
        return f"{self.student} - {self.assignment}"