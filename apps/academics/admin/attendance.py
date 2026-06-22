from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.attendance import AttendanceRecord, AttendanceSummary

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(ModelAdmin):
    list_display = ['student', 'class_assigned', 'date', 'status', 'marked_by']
    list_filter = ['status', 'date']
    search_fields = ['student__user__username', 'class_assigned__name']

@admin.register(AttendanceSummary)
class AttendanceSummaryAdmin(ModelAdmin):
    list_display = ['student', 'term', 'class_assigned', 'attendance_percentage']
    list_filter = ['term']
    search_fields = ['student__user__username']