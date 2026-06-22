from django.db import models
from core.models import BaseModel
from core.choices import RoleChoices, NotificationTypeChoices

class Announcement(BaseModel):
    """School-wide announcement targeting a specific audience."""
    title = models.CharField(max_length=200)
    body = models.TextField()
    audience = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.STUDENT,
        db_index=True,
    )
    published_at = models.DateTimeField(null=True, blank=True)
    is_pinned = models.BooleanField(default=False, db_index=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
    def __str__(self):
        return self.title

class Notification(BaseModel):
    """Per-user system notification."""
    recipient = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="notifications",
        db_index=True,
    )
    notification_type = models.CharField(
        max_length=20,
        choices=NotificationTypeChoices.choices,
        default=NotificationTypeChoices.SYSTEM,
        db_index=True,
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False, db_index=True)
    read_at = models.DateTimeField(null=True, blank=True)
    link = models.URLField(blank=True, default="")
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
    def __str__(self):
        return f"{self.title} for {self.recipient.username}"

class Message(BaseModel):
    """Direct 1-to-1 message between users."""
    sender = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="sent_messages",
        db_index=True,
    )
    recipient = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="received_messages",
        db_index=True,
    )
    subject = models.CharField(max_length=200, blank=True, default="")
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, db_index=True)
    read_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ["-sent_at"]
        verbose_name = "Message"
        verbose_name_plural = "Messages"
    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username}: {self.subject}"

class Question(BaseModel):
    """Student question on a subject for the Q&A board."""
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="questions",
        db_index=True,
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE,
        related_name="questions",
        db_index=True,
    )
    question_text = models.TextField()
    asked_at = models.DateTimeField(auto_now_add=True)
    answer_text = models.TextField(blank=True, default="")
    answered_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="answered_questions",
        db_index=True,
    )
    answered_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ["-asked_at"]
        verbose_name = "Question"
        verbose_name_plural = "Questions"
    def __str__(self):
        return f"Question by {self.student} on {self.subject.name}"

class CareerTalkSession(BaseModel):
    """Alumni career talk session event."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    alumni = models.ForeignKey(
        "people.AlumniProfile",
        on_delete=models.CASCADE,
        related_name="career_talk_sessions",
        db_index=True,
    )
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    max_attendees = models.PositiveIntegerField(default=100)
    registration_deadline = models.DateField()
    class Meta:
        ordering = ["-date"]
        verbose_name = "Career Talk Session"
        verbose_name_plural = "Career Talk Sessions"
    def __str__(self):
        return self.title