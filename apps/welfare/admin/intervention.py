from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.welfare.models.intervention import InterventionCase, InterventionNote, Absence, WelfareReport


@admin.register(InterventionCase)
class InterventionCaseAdmin(ModelAdmin):
    list_display = ('student', 'case_type', 'status', 'opened_at', 'closed_at')
    list_filter = ('status', 'case_type')
    search_fields = ('student__user__username', 'description')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')

@admin.register(InterventionNote)
class InterventionNoteAdmin(ModelAdmin):
    list_display = ('case', 'added_by', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('note',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')

@admin.register(Absence)
class AbsenceAdmin(ModelAdmin):
    list_display = ('student', 'from_date', 'to_date', 'is_excused', 'parent_notified')
    list_filter = ('is_excused', 'parent_notified', 'from_date')
    search_fields = ('student__user__username', 'reason')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')

@admin.register(WelfareReport)
class WelfareReportAdmin(ModelAdmin):
    list_display = ('student', 'term', 'overall_welfare_level', 'prepared_by')
    list_filter = ('term', 'overall_welfare_level')
    search_fields = ('student__user__username', 'recommendations')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')