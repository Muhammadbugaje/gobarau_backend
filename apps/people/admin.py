from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.people.models import (
    StudentProfile, TeacherProfile, ParentProfile, AlumniProfile,
    ClassEnrollment, WardRelationship
)


@admin.register(StudentProfile)
class StudentProfileAdmin(ModelAdmin):
    list_display = ['admission_number', 'person', 'enrollment_status', 'class_assigned', 'date_admitted']
    list_filter = ['enrollment_status', 'wing', 'campus']
    search_fields = ['admission_number', 'person__first_name', 'person__last_name']
    raw_id_fields = ['person', 'class_assigned', 'wing', 'campus']


@admin.register(TeacherProfile)
class TeacherProfileAdmin(ModelAdmin):
    list_display = ['staff_number', 'person', 'is_active']
    list_filter = ['is_active']
    search_fields = ['staff_number', 'person__first_name', 'person__last_name']
    raw_id_fields = ['person']


@admin.register(ParentProfile)
class ParentProfileAdmin(ModelAdmin):
    list_display = ['person', 'is_primary_guardian']
    list_filter = ['is_primary_guardian']
    search_fields = ['person__first_name', 'person__last_name']
    raw_id_fields = ['person']


@admin.register(AlumniProfile)
class AlumniProfileAdmin(ModelAdmin):
    list_display = ['person', 'graduation_year', 'is_verified', 'is_available_for_mentorship']
    list_filter = ['graduation_year', 'is_verified', 'is_available_for_mentorship']
    search_fields = ['person__first_name', 'person__last_name']
    raw_id_fields = ['person', 'student_profile', 'final_class']


@admin.register(ClassEnrollment)
class ClassEnrollmentAdmin(ModelAdmin):
    list_display = ['student', 'class_assigned', 'session', 'term', 'is_active']
    list_filter = ['session', 'term', 'is_active']
    search_fields = ['student__admission_number', 'class_assigned__name']


@admin.register(WardRelationship)
class WardRelationshipAdmin(ModelAdmin):
    list_display = ['parent', 'student', 'relationship_type', 'is_primary_guardian']
    list_filter = ['is_primary_guardian']
    search_fields = ['parent__person__first_name', 'student__admission_number']