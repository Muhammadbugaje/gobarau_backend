from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.subjects import Subject, TeacherClassSubject

@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ['name', 'code', 'department', 'subject_type']
    list_filter = ['subject_type', 'department']
    search_fields = ['name', 'code']

@admin.register(TeacherClassSubject)
class TeacherClassSubjectAdmin(ModelAdmin):
    list_display = ['teacher', 'class_assigned', 'subject', 'is_form_teacher', 'academic_year']
    list_filter = ['is_form_teacher', 'academic_year']
    search_fields = ['teacher__user__username', 'class_assigned__name', 'subject__name']