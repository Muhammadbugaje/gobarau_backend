from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.communication.models import Announcement, Notification, Message, Question, CareerTalkSession

@admin.register(Announcement)
class AnnouncementAdmin(ModelAdmin):
    list_display = ('title', 'audience', 'published_at', 'is_pinned', 'expires_at')
    list_filter = ('audience', 'is_pinned')
    search_fields = ('title', 'body')

@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ('recipient', 'notification_type', 'title', 'is_read', 'read_at')
    list_filter = ('notification_type', 'is_read')
    search_fields = ('recipient__username', 'title', 'message')

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('sender__username', 'recipient__username', 'subject', 'body')

@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('student', 'subject', 'asked_at', 'answered_by', 'answered_at')
    list_filter = ('subject', 'asked_at')
    search_fields = ('student__user__username', 'question_text', 'answer_text')

@admin.register(CareerTalkSession)
class CareerTalkSessionAdmin(ModelAdmin):
    list_display = ('title', 'alumni', 'date', 'time', 'venue', 'max_attendees')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'venue')