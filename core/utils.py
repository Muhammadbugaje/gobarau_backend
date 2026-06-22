import re
from django.apps import apps
from django.utils import timezone
from django.utils.text import slugify as django_slugify


def generate_admission_number():
    """Generate unique admission number: GAK/YYYY/NNN."""
    year = timezone.now().year
    prefix = f"GAK/{year}/"
    try:
        StudentProfile = apps.get_model("people", "StudentProfile")
        last = (
            StudentProfile.objects.filter(admission_number__startswith=prefix)
            .order_by("-admission_number")
            .values_list("admission_number", flat=True)
            .first()
        )
        seq = int(last.split("/")[-1]) + 1 if last else 1
    except LookupError:
        seq = 1
    return f"{prefix}{seq:03d}"
def generate_staff_number():
    """Generate unique staff number: STAFF/YYYY/NNN."""
    year = timezone.now().year
    prefix = f"STAFF/{year}/"
    try:
        TeacherProfile = apps.get_model("people", "TeacherProfile")
        last = (
            TeacherProfile.objects.filter(staff_number__startswith=prefix)
            .order_by("-staff_number")
            .values_list("staff_number", flat=True)
            .first()
        )
        seq = int(last.split("/")[-1]) + 1 if last else 1
    except LookupError:
        seq = 1
    return f"{prefix}{seq:03d}"
def generate_receipt_number():
    """Generate unique receipt number: RCPT/YYYY/NNN."""
    year = timezone.now().year
    prefix = f"RCPT/{year}/"
    try:
        Payment = apps.get_model("finance", "Payment")
        last = (
            Payment.objects.filter(receipt_number__startswith=prefix)
            .order_by("-receipt_number")
            .values_list("receipt_number", flat=True)
            .first()
        )
        seq = int(last.split("/")[-1]) + 1 if last else 1
    except LookupError:
        seq = 1
    return f"{prefix}{seq:03d}"
def validate_nigerian_phone(phone):
    """Validate Nigerian phone: 0XXXXXXXXXX or +234XXXXXXXXXX."""
    pattern = r"^(0\d{10}|\+234\d{10})$"
    return bool(re.match(pattern, phone or ""))
def slugify(text):
    """Slugify text for content titles."""
    return django_slugify(text)