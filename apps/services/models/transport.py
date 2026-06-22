from django.db import models
from core.models import BaseModel, AuditMixin
from core.choices import TransportDirectionChoices


class BusRoute(BaseModel):
    """Transport route definition."""
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    stops = models.JSONField(default=list, blank=True)
    distance_km = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    class Meta:
        ordering = ["name"]
        verbose_name = "Bus Route"
        verbose_name_plural = "Bus Routes"
    def __str__(self):
        return self.name

class BusVehicle(BaseModel):
    """School bus details."""
    registration_number = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField(default=30)
    driver = models.ForeignKey(
        "accounts.Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="driven_vehicles",
        db_index=True,
    )
    route = models.ForeignKey(
        "services.BusRoute",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vehicles",
        db_index=True,
    )
    class Meta:
        ordering = ["registration_number"]
        verbose_name = "Bus Vehicle"
        verbose_name_plural = "Bus Vehicles"
    def __str__(self):
        return self.registration_number

class TransportSubscription(AuditMixin):
    """Student enrollment in school transport."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="transport_subscriptions",
        db_index=True,
    )
    route = models.ForeignKey(
        "services.BusRoute",
        on_delete=models.CASCADE,
        related_name="subscriptions",
        db_index=True,
    )
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="transport_subscriptions",
        db_index=True,
    )
    direction = models.CharField(
        max_length=20,
        choices=TransportDirectionChoices.choices,
        default=TransportDirectionChoices.BOTH,
        db_index=True,
    )
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Transport Subscription"
        verbose_name_plural = "Transport Subscriptions"
        unique_together = ("student", "session", "route")
    def __str__(self):
        return f"{self.student} - {self.route.name}"