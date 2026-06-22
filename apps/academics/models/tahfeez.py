from django.db import models
from core.models import BaseModel
from core.choices import JuzStatusChoices

class JuzProgress(BaseModel):
    """Tracks a student's memorization progress for a Juz in Tahfeez."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="juz_progresses",
        db_index=True,
    )
    juz_number = models.PositiveIntegerField(db_index=True)
    surah_start = models.CharField(max_length=50)
    surah_end = models.CharField(max_length=50)
    ayat_start = models.PositiveIntegerField()
    ayat_end = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=JuzStatusChoices.choices,
        default=JuzStatusChoices.NOT_STARTED,
        db_index=True,
    )
    started_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["juz_number"]
        verbose_name = "Juz Progress"
        verbose_name_plural = "Juz Progresses"
        unique_together = ("student", "juz_number")

    def __str__(self):
        return f"{self.student} - Juz {self.juz_number} - {self.status}"

class RecitationSession(BaseModel):
    """Record of a student's recitation session with a teacher."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="recitation_sessions",
        db_index=True,
    )
    teacher = models.ForeignKey(
        "people.TeacherProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recitation_sessions",
        db_index=True,
    )
    date = models.DateField(db_index=True)
    juz_covered = models.CharField(max_length=100)
    surah_covered = models.CharField(max_length=100)
    quality_rating = models.PositiveIntegerField(default=5)  # 1-5 scale
    remarks = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-date"]
        verbose_name = "Recitation Session"
        verbose_name_plural = "Recitation Sessions"

    def __str__(self):
        return f"{self.student} - {self.date} Session"