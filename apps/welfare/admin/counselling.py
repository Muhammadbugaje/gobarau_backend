from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.welfare.models.counselling import CounsellingSession


@admin.register(CounsellingSession)
class CounsellingSessionAdmin(ModelAdmin):
    list_display = ('student', 'counsellor', 'session_date', 'follow_up_date')
    list_filter = ('session_date', 'follow_up_date')
    search_fields = ('student__user__username', 'presenting_issue', 'notes')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')