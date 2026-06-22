from django.core.exceptions import ValidationError
from django.db import models
from core.choices import EducationTierChoices, TermChoices, WingChoices
from core.models import AuditMixin, BaseModel


class SchoolSettings(AuditMixin):
    """Singleton model for school-wide configuration."""
    name = models.CharField(max_length=200)
    motto = models.CharField(max_length=200, blank=True, default="")
    logo = models.ImageField(upload_to="school/", blank=True, null=True)
    address = models.TextField(blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=20, blank=True, default="")
    academic_year = models.CharField(max_length=20, blank=True, default="")
    class Meta:
        ordering = ["name"]
        verbose_name = "School Settings"
        verbose_name_plural = "School Settings"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.pk and SchoolSettings.objects.exists():
            raise ValidationError("Only one SchoolSettings instance is allowed.")
        super().save(*args, **kwargs)
class AcademicSession(BaseModel):
    """Academic session (e.g. 2025/2026)."""
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False, db_index=True)
    class Meta:
        ordering = ["-start_date"]
        verbose_name = "Academic Session"
        verbose_name_plural = "Academic Sessions"
    def __str__(self):
        return self.name
class Term(BaseModel):
    """Term within an academic session."""
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="terms",
        db_index=True,
    )
    name = models.CharField(max_length=10, choices=TermChoices.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False, db_index=True)
    class Meta:
        ordering = ["session", "name"]
        verbose_name = "Term"
        verbose_name_plural = "Terms"
        unique_together = ("session", "name")
    def __str__(self):
        return f"{self.session} — {self.get_name_display()}"
class Wing(BaseModel):
    """School wing: Regular, Islamiyyah, Tahfeez."""
    name = models.CharField(max_length=20, choices=WingChoices.choices)
    color_code = models.CharField(max_length=7, blank=True, default="")
    description = models.TextField(blank=True, default="")
    class Meta:
        ordering = ["name"]
        verbose_name = "Wing"
        verbose_name_plural = "Wings"
    def __str__(self):
        return self.get_name_display()
class Campus(BaseModel):
    """Physical campus location."""
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True, default="")
    phone = models.CharField(max_length=20, blank=True, default="")
    principal = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="campuses",
        db_index=True,
    )
    is_main = models.BooleanField(default=False, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ["name"]
        verbose_name = "Campus"
        verbose_name_plural = "Campuses"
    def __str__(self):
        return self.name
class Department(BaseModel):
    """Academic department."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    head = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="departments",
        db_index=True,
    )
    class Meta:
        ordering = ["name"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"
    def __str__(self):
        return self.name
class ClassLevel(BaseModel):
    """Class level (e.g. JSS 1, SS 2)."""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    order_index = models.PositiveIntegerField(default=0)
    education_tier = models.CharField(
        max_length=10,
        choices=EducationTierChoices.choices,
        default=EducationTierChoices.PRIMARY,
        db_index=True,
    )
    class Meta:
        ordering = ["order_index", "name"]
        verbose_name = "Class Level"
        verbose_name_plural = "Class Levels"
    def __str__(self):
        return self.name
class GradingScale(AuditMixin):
    """Grading scale for a session."""
    name = models.CharField(max_length=200)
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="grading_scales",
        db_index=True,
    )
    is_active = models.BooleanField(default=False, db_index=True)
    class Meta:
        ordering = ["name"]
        verbose_name = "Grading Scale"
        verbose_name_plural = "Grading Scales"
    def __str__(self):
        return self.name
class GradingBand(BaseModel):
    """Grade band within a grading scale."""
    grading_scale = models.ForeignKey(
        "administration.GradingScale",
        on_delete=models.CASCADE,
        related_name="bands",
        db_index=True,
    )
    min_score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5)
    grade_point = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    remark = models.CharField(max_length=200, blank=True, default="")
    class Meta:
        ordering = ["-max_score"]
        verbose_name = "Grading Band"
        verbose_name_plural = "Grading Bands"
    def __str__(self):
        return f"{self.grade} ({self.min_score}–{self.max_score})"
    def clean(self):
        if self.min_score > self.max_score:
            raise ValidationError({"min_score": "Minimum score cannot exceed maximum score."})