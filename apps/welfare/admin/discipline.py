from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.welfare.models.discipline import DisciplinaryRecord, MeritDeduction


@admin.register(DisciplinaryRecord)
class DisciplinaryRecordAdmin(ModelAdmin):
    list_display = ('student', 'incident_date', 'incident_type', 'status')
    list_filter = ('status', 'incident_date', 'incident_type')
    search_fields = ('student__user__username', 'description', 'action_taken')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')

@admin.register(MeritDeduction)
class MeritDeductionAdmin(ModelAdmin):
    list_display = ('student', 'points', 'direction', 'reason', 'recorded_by')
    list_filter = ('direction',)
    search_fields = ('student__user__username', 'reason')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')