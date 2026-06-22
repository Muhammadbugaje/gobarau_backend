"""
People app — all role profiles and person-centric models.
"""
from django.db import models
from core.models import BaseModel, SoftDeleteModel, AuditMixin
from core.choices import (
    GenderChoices, NIGERIAN_STATES, EnrollmentStatusChoices,
    RoleChoices, WingChoices
)


# ---------- Student Profile ----------
class StudentProfile(SoftDeleteModel, AuditMixin):
    """Student role profile — linked to Person."""
    person = models.OneToOneField(
        'accounts.Person',
        on_delete=models.CASCADE,
        related_name='student_profile',
        db_index=True,
    )
    admission_number = models.CharField(max_length=20, unique=True, db_index=True)
    enrollment_status = models.CharField(
        max_length=20,
        choices=EnrollmentStatusChoices.choices,
        default=EnrollmentStatusChoices.ACTIVE,
        db_index=True,
    )
    date_admitted = models.DateField(null=True, blank=True)
    class_assigned = models.ForeignKey(
        'academics.Class',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        db_index=True,
    )
    wing = models.ForeignKey(
        'administration.Wing',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        db_index=True,
    )
    campus = models.ForeignKey(
        'administration.Campus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        db_index=True,
    )

    class Meta:
        ordering = ['admission_number']
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Student Profiles'

    def __str__(self):
        return f"{self.person.full_name} ({self.admission_number})"


# ---------- Teacher Profile ----------
class TeacherProfile(SoftDeleteModel, AuditMixin):
    """Teacher role profile — linked to Person."""
    person = models.OneToOneField(
        'accounts.Person',
        on_delete=models.CASCADE,
        related_name='teacher_profile',
        db_index=True,
    )
    staff_number = models.CharField(max_length=20, unique=True, db_index=True)
    date_employed = models.DateField(null=True, blank=True)
    qualification = models.CharField(max_length=200, blank=True)
    specialization = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)
    show_on_website = models.BooleanField(default=True)

    class Meta:
        ordering = ['staff_number']
        verbose_name = 'Teacher Profile'
        verbose_name_plural = 'Teacher Profiles'

    def __str__(self):
        return f"{self.person.full_name} ({self.staff_number})"


# ---------- Parent Profile ----------
class ParentProfile(SoftDeleteModel, AuditMixin):
    """Parent/guardian role profile — linked to Person."""
    person = models.OneToOneField(
        'accounts.Person',
        on_delete=models.CASCADE,
        related_name='parent_profile',
        db_index=True,
    )
    occupation = models.CharField(max_length=200, blank=True)
    employer = models.CharField(max_length=200, blank=True)
    is_primary_guardian = models.BooleanField(default=False)

    class Meta:
        ordering = ['person__last_name', 'person__first_name']
        verbose_name = 'Parent Profile'
        verbose_name_plural = 'Parent Profiles'

    def __str__(self):
        return f"{self.person.full_name} (Parent)"


# ---------- Alumni Profile ----------
class AlumniProfile(SoftDeleteModel, AuditMixin):
    """Alumni role profile — linked to Person."""
    person = models.OneToOneField(
        'accounts.Person',
        on_delete=models.CASCADE,
        related_name='alumni_profile',
        db_index=True,
    )
    student_profile = models.OneToOneField(
        'people.StudentProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alumni_profile',
        db_index=True,
    )
    graduation_year = models.PositiveIntegerField()
    final_class = models.ForeignKey(
        'academics.Class',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alumni',
        db_index=True,
    )
    career_field = models.CharField(max_length=200, blank=True)
    current_employer = models.CharField(max_length=200, blank=True)
    university_attended = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='Nigeria')
    linkedin_url = models.URLField(blank=True)
    is_available_for_mentorship = models.BooleanField(default=False)
    mentorship_areas = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False, db_index=True)
    is_on_wall_of_fame = models.BooleanField(default=False)

    class Meta:
        ordering = ['-graduation_year', 'person__last_name']
        verbose_name = 'Alumni Profile'
        verbose_name_plural = 'Alumni Profiles'

    def __str__(self):
        return f"{self.person.full_name} (Alumni {self.graduation_year})"


# ---------- Class Enrollment ----------
class ClassEnrollment(BaseModel):
    """Student enrollment in a specific class for a session/term."""
    student = models.ForeignKey(
        'people.StudentProfile',
        on_delete=models.CASCADE,
        related_name='enrollments',
        db_index=True,
    )
    class_assigned = models.ForeignKey(
        'academics.Class',
        on_delete=models.CASCADE,
        related_name='enrollments',
        db_index=True,
    )
    session = models.ForeignKey(
        'administration.AcademicSession',
        on_delete=models.CASCADE,
        related_name='enrollments',
        db_index=True,
    )
    term = models.ForeignKey(
        'administration.Term',
        on_delete=models.CASCADE,
        related_name='enrollments',
        db_index=True,
    )
    date_enrolled = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ['-date_enrolled']
        verbose_name = 'Class Enrollment'
        verbose_name_plural = 'Class Enrollments'
        unique_together = ('student', 'class_assigned', 'session', 'term')

    def __str__(self):
        return f"{self.student} in {self.class_assigned} ({self.session})"


# ---------- Ward Relationship ----------
class WardRelationship(BaseModel):
    """Link between a parent and a student (ward)."""
    parent = models.ForeignKey(
        'people.ParentProfile',
        on_delete=models.CASCADE,
        related_name='wards',
        db_index=True,
    )
    student = models.ForeignKey(
        'people.StudentProfile',
        on_delete=models.CASCADE,
        related_name='guardians',
        db_index=True,
    )
    relationship_type = models.CharField(max_length=50, blank=True)
    is_primary_guardian = models.BooleanField(default=False)
    can_pickup = models.BooleanField(default=True)

    class Meta:
        ordering = ['parent', 'student']
        verbose_name = 'Ward Relationship'
        verbose_name_plural = 'Ward Relationships'
        unique_together = ('parent', 'student')

    def __str__(self):
        return f"{self.parent} - {self.student} ({self.relationship_type})"