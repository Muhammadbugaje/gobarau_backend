from django.db import models
 
class RoleChoices(models.TextChoices):
    SUPER_ADMIN = "super_admin", "Super Admin"
    PRINCIPAL = "principal", "Principal"
    VICE_PRINCIPAL = "vice_principal", "Vice Principal"
    BURSAR = "bursar", "Bursar"
    TEACHER = "teacher", "Teacher"
    STUDENT = "student", "Student"
    PARENT = "parent", "Parent"
    ALUMNI = "alumni", "Alumni"
    NURSE = "nurse", "School Nurse"
    COUNSELLOR = "counsellor", "Counsellor"
    
class WingChoices(models.TextChoices):
    REGULAR = "regular", "Regular"
    ISLAMIYYAH = "islamiyyah", "Islamiyyah"
    TAHFEEZ = "tahfeez", "Tahfeez"

class GenderChoices(models.TextChoices):
    M = "M", "Male"
    F = "F", "Female"

class TermChoices(models.TextChoices):
    FIRST = "first", "First Term"
    SECOND = "second", "Second Term"
    THIRD = "third", "Third Term"

class EnrollmentStatusChoices(models.TextChoices):
    ACTIVE = "active", "Active"
    GRADUATED = "graduated", "Graduated"
    WITHDRAWN = "withdrawn", "Withdrawn"
    TRANSFERRED = "transferred", "Transferred"
    REPEATED = "repeated", "Repeated"

class PaymentStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    PAID = "paid", "Paid"
    PARTIAL = "partial", "Partial"
    OVERDUE = "overdue", "Overdue"
    REFUNDED = "refunded", "Refunded"

class AttendanceStatusChoices(models.TextChoices):
    PRESENT = "present", "Present"
    ABSENT = "absent", "Absent"
    LATE = "late", "Late"
    EXCUSED = "excused", "Excused"

class InterventionTypeChoices(models.TextChoices):
    ACADEMIC = "academic", "Academic"
    ATTENDANCE = "attendance", "Attendance"
    BEHAVIOURAL = "behavioural", "Behavioural"
    WELFARE = "welfare", "Welfare"
    HEALTH = "health", "Health"
    TAHFEEZ = "tahfeez", "Tahfeez"


class SubjectTypeChoices(models.TextChoices):
    CORE = "core", "Core"
    ELECTIVE = "elective", "Elective"
    VOCATIONAL = "vocational", "Vocational"

class DayChoices(models.TextChoices):
    MONDAY = "monday", "Monday"
    TUESDAY = "tuesday", "Tuesday"
    WEDNESDAY = "wednesday", "Wednesday"
    THURSDAY = "thursday", "Thursday"
    FRIDAY = "friday", "Friday"
    SATURDAY = "saturday", "Saturday"
    SUNDAY = "sunday", "Sunday"

class JuzStatusChoices(models.TextChoices):
    NOT_STARTED = "not_started", "Not Started"
    IN_PROGRESS = "in_progress", "In Progress"
    MEMORIZED = "memorized", "Memorized"
    REVIEWED = "reviewed", "Reviewed"

class ApplicationStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"
    WAITLISTED = "waitlisted", "Waitlisted"

class AlumniStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"


class EducationTierChoices(models.TextChoices):
    PRIMARY = "primary", "Primary"
    JSS = "jss", "JSS"
    SSS = "sss", "SSS"
NIGERIAN_STATES = [
    ("abia", "Abia"),
    ("adamawa", "Adamawa"),
    ("akwa_ibom", "Akwa Ibom"),
    ("anambra", "Anambra"),
    ("bauchi", "Bauchi"),
    ("bayelsa", "Bayelsa"),
    ("benue", "Benue"),
    ("borno", "Borno"),
    ("cross_river", "Cross River"),
    ("delta", "Delta"),
    ("ebonyi", "Ebonyi"),
    ("edo", "Edo"),
    ("ekiti", "Ekiti"),
    ("enugu", "Enugu"),
    ("fct", "Federal Capital Territory"),
    ("gombe", "Gombe"),
    ("imo", "Imo"),
    ("jigawa", "Jigawa"),
    ("kaduna", "Kaduna"),
    ("kano", "Kano"),
    ("katsina", "Katsina"),
    ("kebbi", "Kebbi"),
    ("kogi", "Kogi"),
    ("kwara", "Kwara"),
    ("lagos", "Lagos"),
    ("nasarawa", "Nasarawa"),
    ("niger", "Niger"),
    ("ogun", "Ogun"),
    ("ondo", "Ondo"),
    ("osun", "Osun"),
    ("oyo", "Oyo"),
    ("plateau", "Plateau"),
    ("rivers", "Rivers"),
    ("sokoto", "Sokoto"),
    ("taraba", "Taraba"),
    ("yobe", "Yobe"),
    ("zamfara", "Zamfara"),
]

class PaymentMethodChoices(models.TextChoices):
    CASH = "cash", "Cash"
    BANK_TRANSFER = "bank_transfer", "Bank Transfer"
    ONLINE = "online", "Online"
class RequestStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    FULFILLED = "fulfilled", "Fulfilled"
    CANCELLED = "cancelled", "Cancelled"
class NotificationTypeChoices(models.TextChoices):
    SYSTEM = "system", "System"
    PAYMENT = "payment", "Payment"
    ACADEMIC = "academic", "Academic"
    ATTENDANCE = "attendance", "Attendance"
    WELFARE = "welfare", "Welfare"
    MESSAGE = "message", "Message"
    
    
class BorrowStatusChoices(models.TextChoices):
    BORROWED = "borrowed", "Borrowed"
    RETURNED = "returned", "Returned"
    OVERDUE = "overdue", "Overdue"
 
class TransportDirectionChoices(models.TextChoices):
    TO_SCHOOL = "to_school", "To School"
    FROM_SCHOOL = "from_school", "From School"
    BOTH = "both", "Both"
 
class InterventionStatusChoices(models.TextChoices):
    OPEN = "open", "Open"
    ON_HOLD = "on_hold", "On Hold"
    CLOSED = "closed", "Closed"
 
class DisciplinaryStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    RESOLVED = "resolved", "Resolved"
    ESCALATED = "escalated", "Escalated"
 
class MeritDirectionChoices(models.TextChoices):
    ADD = "add", "Add"
    DEDUCT = "deduct", "Deduct"