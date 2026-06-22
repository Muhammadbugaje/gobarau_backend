import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from core.managers import ActiveManager, ArchivedManager, SoftDeleteManager

class BaseModel(models.Model):
    """Abstract base model providing public UUID and timestamps."""
    public_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ["-created_at"]
        
class TimeStampedModel(models.Model):
    """Lightweight abstract model with only timestamps (no UUID)."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ["-created_at"]
        
class SoftDeleteModel(BaseModel):
    """Abstract model with soft-delete (archive) capability."""
    is_archived = models.BooleanField(default=False, db_index=True)
    archived_at = models.DateTimeField(null=True, blank=True)
    archived_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        db_index=True,
    )
    objects = ActiveManager()
    all_objects = SoftDeleteManager()
    archived = ArchivedManager()
    class Meta:
        abstract = True
        ordering = ["-created_at"]
    def archive(self, user=None):
        """Mark this record as archived."""
        self.is_archived = True
        self.archived_at = timezone.now()
        if user and user.is_authenticated:
            self.archived_by = user
        self.save(update_fields=["is_archived", "archived_at", "archived_by"])
    def restore(self):
        """Restore an archived record."""
        self.is_archived = False
        self.archived_at = None
        self.archived_by = None
        self.save(update_fields=["is_archived", "archived_at", "archived_by"])
        
class AuditMixin(BaseModel):
    """Abstract mixin tracking who created/modified a record."""
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        db_index=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        db_index=True,
    )
    class Meta:
        abstract = True
        ordering = ["-created_at"]