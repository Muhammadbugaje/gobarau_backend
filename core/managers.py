from django.db import models


class ActiveManager(models.Manager):
    """Returns only non-archived records."""
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)
class ArchivedManager(models.Manager):
    """Returns only archived records."""
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=True)
class SoftDeleteManager(models.Manager):
    """Returns all records regardless of archive state."""
    def get_queryset(self):
        return super().get_queryset()