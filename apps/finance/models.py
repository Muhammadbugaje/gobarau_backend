from django.db import models
from core.models import BaseModel, AuditMixin
from core.choices import PaymentMethodChoices, PaymentStatusChoices, RequestStatusChoices

class FeeType(BaseModel):
    """Category of fee (e.g., Tuition, ICT Levy, PTA)."""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, default="")
    is_recurring = models.BooleanField(default=False, db_index=True)
    class Meta:
        ordering = ["name"]
        verbose_name = "Fee Type"
        verbose_name_plural = "Fee Types"
    def __str__(self):
        return self.name

class FeeStructure(BaseModel):
    """Fee amount assigned to a specific class level for an academic session."""
    fee_type = models.ForeignKey(
        "finance.FeeType",
        on_delete=models.CASCADE,
        related_name="fee_structures",
        db_index=True,
    )
    class_level = models.ForeignKey(
        "administration.ClassLevel",
        on_delete=models.CASCADE,
        related_name="fee_structures",
        db_index=True,
    )
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="fee_structures",
        db_index=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Fee Structure"
        verbose_name_plural = "Fee Structures"
        unique_together = ("fee_type", "class_level", "session")
    def __str__(self):
        return f"{self.fee_type.name} - {self.class_level.name} - {self.session.name}"

class Payment(AuditMixin):
    """Record of a single payment transaction made by a student."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="payments",
        db_index=True,
    )
    fee_structure = models.ForeignKey(
        "finance.FeeStructure",
        on_delete=models.CASCADE,
        related_name="payments",
        db_index=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method = models.CharField(
        max_length=20,
        choices=PaymentMethodChoices.choices,
        default=PaymentMethodChoices.CASH,
        db_index=True,
    )
    reference = models.CharField(max_length=100, blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PENDING,
        db_index=True,
    )
    receipt_number = models.CharField(max_length=50, unique=True, db_index=True)
    class Meta:
        ordering = ["-payment_date"]
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
    def __str__(self):
        return f"{self.receipt_number} - {self.student} - {self.amount}"

class ScholarshipFund(BaseModel):
    """Scholarship fund available for allocation."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="scholarship_funds",
        db_index=True,
    )
    is_active = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ["name"]
        verbose_name = "Scholarship Fund"
        verbose_name_plural = "Scholarship Funds"
    def __str__(self):
        return f"{self.name} ({self.session.name})"

class ScholarshipRecipient(AuditMixin):
    """Record of a scholarship awarded to a student."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="scholarships",
        db_index=True,
    )
    scholarship = models.ForeignKey(
        "finance.ScholarshipFund",
        on_delete=models.CASCADE,
        related_name="recipients",
        db_index=True,
    )
    amount_awarded = models.DecimalField(max_digits=10, decimal_places=2)
    awarded_date = models.DateField()
    class Meta:
        ordering = ["-awarded_date"]
        verbose_name = "Scholarship Recipient"
        verbose_name_plural = "Scholarship Recipients"
        unique_together = ("student", "scholarship")
    def __str__(self):
        return f"{self.student} - {self.scholarship.name}"

class ItemCategory(BaseModel):
    """Category for marketplace items."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    class Meta:
        ordering = ["name"]
        verbose_name = "Item Category"
        verbose_name_plural = "Item Categories"
    def __str__(self):
        return self.name

class MarketplaceItem(BaseModel):
    """Items sold in the school marketplace."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    category = models.ForeignKey(
        "finance.ItemCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="items",
        db_index=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ["name"]
        verbose_name = "Marketplace Item"
        verbose_name_plural = "Marketplace Items"
    def __str__(self):
        return self.name

class MarketplaceRequest(BaseModel):
    """Student request for marketplace items."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="marketplace_requests",
        db_index=True,
    )
    items = models.ManyToManyField(
        "finance.MarketplaceItem",
        through="finance.RequestItem",
        related_name="requests"
    )
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.PENDING,
        db_index=True,
    )
    class Meta:
        ordering = ["-request_date"]
        verbose_name = "Marketplace Request"
        verbose_name_plural = "Marketplace Requests"
    def __str__(self):
        return f"Request by {self.student} on {self.request_date}"

class RequestItem(BaseModel):
    """Line item linking a marketplace request to an item with quantity and price."""
    request = models.ForeignKey(
        "finance.MarketplaceRequest",
        on_delete=models.CASCADE,
        related_name="request_items",
        db_index=True,
    )
    item = models.ForeignKey(
        "finance.MarketplaceItem",
        on_delete=models.CASCADE,
        related_name="request_items",
        db_index=True,
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Request Item"
        verbose_name_plural = "Request Items"
        unique_together = ("request", "item")
    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

class RestockLog(AuditMixin):
    """History log for restocking marketplace items."""
    item = models.ForeignKey(
        "finance.MarketplaceItem",
        on_delete=models.CASCADE,
        related_name="restock_logs",
        db_index=True,
    )
    quantity_added = models.PositiveIntegerField()
    previous_stock = models.PositiveIntegerField()
    new_stock = models.PositiveIntegerField()
    restocked_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-restocked_at"]
        verbose_name = "Restock Log"
        verbose_name_plural = "Restock Logs"
    def __str__(self):
        return f"Restocked {self.item.name}: +{self.quantity_added}"
