from django.db import models
from core.models import BaseModel, AuditMixin
from core.choices import BorrowStatusChoices


class Book(BaseModel):
    """Library book inventory."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, default="")
    isbn = models.CharField(max_length=20, unique=True, blank=True, default="")
    genre = models.CharField(max_length=100, blank=True, default="")
    quantity_total = models.PositiveIntegerField(default=1)
    quantity_available = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=100, blank=True, default="")
    class Meta:
        ordering = ["title"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
    def __str__(self):
        return self.title

class BorrowRecord(AuditMixin):
    """Record tracking a borrowed book."""
    book = models.ForeignKey(
        "services.Book",
        on_delete=models.CASCADE,
        related_name="borrow_records",
        db_index=True,
    )
    borrower = models.ForeignKey(
        "accounts.Person",
        on_delete=models.CASCADE,
        related_name="borrow_records",
        db_index=True,
    )
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=BorrowStatusChoices.choices,
        default=BorrowStatusChoices.BORROWED,
        db_index=True,
    )
    class Meta:
        ordering = ["-borrow_date"]
        verbose_name = "Borrow Record"
        verbose_name_plural = "Borrow Records"
    def __str__(self):
        return f"{self.borrower} borrowed {self.book}"

class LibraryFine(BaseModel):
    """Fine levied for overdue books."""
    borrow_record = models.ForeignKey(
        "services.BorrowRecord",
        on_delete=models.CASCADE,
        related_name="fines",
        db_index=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False, db_index=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Library Fine"
        verbose_name_plural = "Library Fines"
    def __str__(self):
        return f"Fine for {self.borrow_record} - {self.amount}"