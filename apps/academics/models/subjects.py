from django.db import models
from core.models import BaseModel
from core.choices import SubjectTypeChoices

class Subject(BaseModel):
    """Academic subject taught in the school."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        "administration.Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subjects",
        db_index=True,
    )
    subject_type = models.CharField(
        max_length=20,
        choices=SubjectTypeChoices.choices,
        default=SubjectTypeChoices.CORE,
        db_index=True,
    )
    description = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["name"]
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name

class TeacherClassSubject(BaseModel):
    """Maps a teacher to a class and subject, indicating teaching assignment."""
    teacher = models.ForeignKey(
        "people.TeacherProfile",
        on_delete=models.CASCADE,
        related_name="class_subjects",
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        "academics.Class",
        on_delete=models.CASCADE,
        related_name="teacher_subjects",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="class_teachers",
        db_index=True,
    )
    is_form_teacher = models.BooleanField(default=False)
    academic_year = models.CharField(max_length=20)

    class Meta:
        ordering = ["class_assigned", "subject"]
        verbose_name = "Teacher Class Subject"
        verbose_name_plural = "Teacher Class Subjects"
        unique_together = ("teacher", "class_assigned", "subject", "academic_year")

    def __str__(self):
        return f"{self.teacher} - {self.class_assigned} - {self.subject}"