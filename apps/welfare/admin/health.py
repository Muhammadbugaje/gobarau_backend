from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.welfare.models.health import HealthProfile, ClinicVisit, Medication


@admin.register(HealthProfile)
class HealthProfileAdmin(ModelAdmin):
    list_display = ('student', 'blood_group', 'genotype', 'created_at')
    search_fields = ('student__user__username', 'allergies', 'chronic_conditions')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')

@admin.register(ClinicVisit)
class ClinicVisitAdmin(ModelAdmin):
    list_display = ('student', 'visit_date', 'referred_out')
    list_filter = ('referred_out', 'visit_date')
    search_fields = ('student__user__username', 'complaint', 'diagnosis')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')

@admin.register(Medication)
class MedicationAdmin(ModelAdmin):
    list_display = ('clinic_visit', 'drug_name', 'dosage', 'frequency', 'duration')
    search_fields = ('drug_name',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'is_archived', 'archived_at', 'archived_by')