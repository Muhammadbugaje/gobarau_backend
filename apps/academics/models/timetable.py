from django.db import models
from core.models import BaseModel
from core.choices import DayChoices

class Timetable(BaseModel):
    """Weekly timetable entry for a class."""
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="timetable_entries",
        db_index=True,
    )
    teacher = models.ForeignKey(
        "people.TeacherProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="timetable_entries",
        db_index=True,
    )
    day = models.CharField(
        max_length=10,
        choices=DayChoices.choices,
        db_index=True,
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True, default="")
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ["day", "start_time"]
        verbose_name = "Timetable"
        verbose_name_plural = "Timetables"

    def __str__(self):
        return f"{self.class_assigned} - {self.subject} - {self.day}"

class ExamTimetable(BaseModel):
    """Examination timetable entry for a class."""
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="exam_timetable_entries",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="exam_timetable_entries",
        db_index=True,
    )
    term = models.ForeignKey(
        "administration.Term",
        on_delete=models.CASCADE,
        related_name="exam_timetable_entries",
        db_index=True,
    )
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["exam_date", "start_time"]
        verbose_name = "Exam Timetable"
        verbose_name_plural = "Exam Timetables"

    def __str__(self):
        return f"{self.class_assigned} - {self.subject} - {self.exam_date}"