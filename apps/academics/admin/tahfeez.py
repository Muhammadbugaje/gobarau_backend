from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.tahfeez import JuzProgress, RecitationSession

@admin.register(JuzProgress)
class JuzProgressAdmin(ModelAdmin):
    list_display = ['student', 'juz_number', 'status', 'started_date', 'completed_date']
    list_filter = ['status', 'juz_number']
    search_fields = ['student__user__username']

@admin.register(RecitationSession)
class RecitationSessionAdmin(ModelAdmin):
    list_display = ['student', 'teacher', 'date', 'quality_rating']
    list_filter = ['date', 'quality_rating']
    search_fields = ['student__user__username', 'teacher__user__username']