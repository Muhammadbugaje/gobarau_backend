from django.contrib.auth.models import AbstractUser
from django.db import models
from core.choices import GenderChoices, NIGERIAN_STATES, RoleChoices, WingChoices
from core.models import AuditMixin, SoftDeleteModel

class User(AbstractUser):
    """Custom user model with role and wing assignment."""
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.STUDENT,
        db_index=True,
    )
    wing = models.CharField(
        max_length=20,
        choices=WingChoices.choices,
        default=WingChoices.REGULAR,
        db_index=True,
    )
    is_verified = models.BooleanField(default=False)
    preferences = models.JSONField(default=dict, blank=True)
    class Meta:
        ordering = ["username"]
        verbose_name = "User"
        verbose_name_plural = "Users"
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Person(SoftDeleteModel, AuditMixin):
    """Single identity record for every human in the system."""
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="person",
        db_index=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, default="")
    preferred_name = models.CharField(max_length=100, blank=True, default="")
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        blank=True,
        default="",
    )
    state_of_origin = models.CharField(
        max_length=50,
        choices=NIGERIAN_STATES,
        blank=True,
        default="",
    )
    lga = models.CharField(max_length=100, blank=True, default="")
    religion = models.CharField(max_length=50, blank=True, default="")
    nationality = models.CharField(max_length=50, default="Nigerian")
    phone_primary = models.CharField(
        max_length=20, blank=True, default="", db_index=True
    )
    phone_secondary = models.CharField(max_length=20, blank=True, default="")
    email_personal = models.EmailField(blank=True, default="")
    address = models.TextField(blank=True, default="")
    photo = models.ImageField(upload_to="people/photos/", blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, default="")
    external_ref = models.CharField(max_length=100, blank=True, default="")
    language = models.CharField(max_length=50, default="English")
    metadata = models.JSONField(default=dict, blank=True)
    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Person"
        verbose_name_plural = "People"
        indexes = [
            models.Index(fields=["last_name", "first_name"]),
            models.Index(fields=["phone_primary"]),
        ]
    def __str__(self):
        return self.full_name
    @property
    def full_name(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(p for p in parts if p).strip()