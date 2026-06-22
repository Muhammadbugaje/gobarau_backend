from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.admissions.models import Application, EntranceExam, AlumniRegistration

@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = ['applicant_name', 'session', 'class_applied_for', 'status', 'submitted_at']
    list_filter = ['status', 'session', 'wing']
    search_fields = ['applicant_name', 'phone', 'email']

@admin.register(EntranceExam)
class EntranceExamAdmin(ModelAdmin):
    list_display = ['application', 'exam_date', 'venue', 'score', 'is_passed']
    list_filter = ['is_passed', 'exam_date']
    search_fields = ['application__applicant_name']

@admin.register(AlumniRegistration)
class AlumniRegistrationAdmin(ModelAdmin):
    list_display = ['student_profile', 'graduation_year', 'career_field', 'status', 'submitted_at']
    list_filter = ['status', 'graduation_year']
    search_fields = ['student_profile__user__username', 'current_employer']