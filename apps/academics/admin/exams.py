from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.exams import ExamRegistration, ExamResult

@admin.register(ExamRegistration)
class ExamRegistrationAdmin(ModelAdmin):
    list_display = ['student', 'subject', 'term', 'class_assigned', 'is_registered']
    list_filter = ['term', 'is_registered']
    search_fields = ['student__user__username', 'subject__name']

@admin.register(ExamResult)
class ExamResultAdmin(ModelAdmin):
    list_display = ['student', 'subject', 'term', 'class_assigned', 'score', 'grade']
    list_filter = ['term', 'grade']
    search_fields = ['student__user__username', 'subject__name']