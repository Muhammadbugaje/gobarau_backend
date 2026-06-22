from django.db import models
from core.models import SoftDeleteModel, AuditMixin

class HealthProfile(SoftDeleteModel, AuditMixin):
    """Sensitive: Student health profile. Restrict access to IsSchoolNurse."""
    student = models.OneToOneField(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="health_profile",
        db_index=True,
    )
    blood_group = models.CharField(max_length=10, blank=True, default="")
    genotype = models.CharField(max_length=10, blank=True, default="")
    allergies = models.TextField(blank=True, default="")
    chronic_conditions = models.TextField(blank=True, default="")
    emergency_contact_name = models.CharField(max_length=200, blank=True, default="")
    emergency_contact_phone = models.CharField(max_length=20, blank=True, default="")
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Health Profile"
        verbose_name_plural = "Health Profiles"
    def __str__(self):
        return f"Health Profile for {self.student}"

class ClinicVisit(SoftDeleteModel, AuditMixin):
    """Audited: Clinic visit record. Track who accessed."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="clinic_visits",
        db_index=True,
    )
    visit_date = models.DateField()
    complaint = models.TextField()
    diagnosis = models.TextField(blank=True, default="")
    treatment = models.TextField(blank=True, default="")
    referred_out = models.BooleanField(default=False)
    class Meta:
        ordering = ["-visit_date"]
        verbose_name = "Clinic Visit"
        verbose_name_plural = "Clinic Visits"
    def __str__(self):
        return f"{self.student} - {self.visit_date}"

class Medication(SoftDeleteModel, AuditMixin):
    """Sensitive: Medication prescribed during a clinic visit."""
    clinic_visit = models.ForeignKey(
        "welfare.ClinicVisit",
        on_delete=models.CASCADE,
        related_name="medications",
        db_index=True,
    )
    drug_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Medication"
        verbose_name_plural = "Medications"
    def __str__(self):
        return f"{self.drug_name} ({self.dosage})"