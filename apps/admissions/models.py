from django.db import models
from core.models import BaseModel
from core.choices import GenderChoices, NIGERIAN_STATES, ApplicationStatusChoices, AlumniStatusChoices

class Application(BaseModel):
    """Application for admission by a prospective student."""
    applicant_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        blank=True,
        default="",
    )
    phone = models.CharField(max_length=20, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    address = models.TextField(blank=True, default="")
    state_of_origin = models.CharField(
        max_length=50,
        choices=NIGERIAN_STATES,
        blank=True,
        default="",
    )
    lga = models.CharField(max_length=100, blank=True, default="")
    religion = models.CharField(max_length=50, blank=True, default="")
    wing = models.ForeignKey(
        "administration.Wing",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="applications",
        db_index=True,
    )
    class_applied_for = models.ForeignKey(
        "administration.ClassLevel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="applications",
        db_index=True,
    )
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="applications",
        db_index=True,
    )
    status = models.CharField(
        max_length=20,
        choices=ApplicationStatusChoices.choices,
        default=ApplicationStatusChoices.PENDING,
        db_index=True,
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_applications",
        db_index=True,
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return f"{self.applicant_name} - {self.session}"

class EntranceExam(BaseModel):
    """Entrance exam details and score for an application."""
    application = models.ForeignKey(
        "admissions.Application",
        on_delete=models.CASCADE,
        related_name="entrance_exams",
        db_index=True,
    )
    exam_date = models.DateField()
    venue = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_passed = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-exam_date"]
        verbose_name = "Entrance Exam"
        verbose_name_plural = "Entrance Exams"

    def __str__(self):
        return f"{self.application.applicant_name} - {self.exam_date}"

class AlumniRegistration(BaseModel):
    """Registration details for alumni."""
    student_profile = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="alumni_registrations",
        db_index=True,
    )
    graduation_year = models.PositiveIntegerField()
    career_field = models.CharField(max_length=200, blank=True, default="")
    current_employer = models.CharField(max_length=200, blank=True, default="")
    university_attended = models.CharField(max_length=200, blank=True, default="")
    city = models.CharField(max_length=100, blank=True, default="")
    country = models.CharField(max_length=100, default="Nigeria")
    linkedin_url = models.URLField(blank=True, default="")
    message = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=AlumniStatusChoices.choices,
        default=AlumniStatusChoices.PENDING,
        db_index=True,
    )
    reviewed_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_alumni",
        db_index=True,
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Alumni Registration"
        verbose_name_plural = "Alumni Registrations"

    def __str__(self):
        return f"{self.student_profile} - {self.graduation_year}"