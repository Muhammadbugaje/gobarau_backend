from django.db import models
from core.models import BaseModel
from core.choices import AttendanceStatusChoices

class AttendanceRecord(BaseModel):
    """Daily attendance record for a student."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="attendance_records",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="attendance_records",
        db_index=True,
    )
    date = models.DateField(db_index=True)
    status = models.CharField(
        max_length=10,
        choices=AttendanceStatusChoices.choices,
        default=AttendanceStatusChoices.PRESENT,
        db_index=True,
    )
    remarks = models.TextField(blank=True, default="")
    marked_by = models.ForeignKey(
        "people.TeacherProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="marked_attendance",
        db_index=True,
    )

    class Meta:
        ordering = ["-date"]
        verbose_name = "Attendance Record"
        verbose_name_plural = "Attendance Records"
        unique_together = ("student", "date", "class_assigned")

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class AttendanceSummary(BaseModel):
    """Termly attendance summary for a student."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="attendance_summaries",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="attendance_summaries",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="attendance_summaries",
        db_index=True,
    )
    total_present = models.PositiveIntegerField(default=0)
    total_absent = models.PositiveIntegerField(default=0)
    total_late = models.PositiveIntegerField(default=0)
    total_excused = models.PositiveIntegerField(default=0)
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ["-attendance_percentage"]
        verbose_name = "Attendance Summary"
        verbose_name_plural = "Attendance Summaries"
        unique_together = ("student", "term", "class_assigned")

    def __str__(self):
        return f"{self.student} - {self.term} Summary"