from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.scores import Score, ReportCard, Assignment, AssignmentSubmission

@admin.register(Score)
class ScoreAdmin(ModelAdmin):
    list_display = ['student', 'subject', 'term', 'class_assigned', 'total_score', 'grade', 'is_locked']
    list_filter = ['term', 'is_locked', 'grade']
    search_fields = ['student__user__username', 'subject__name']

@admin.register(ReportCard)
class ReportCardAdmin(ModelAdmin):
    list_display = ['student', 'term', 'class_assigned', 'average', 'position', 'is_published']
    list_filter = ['term', 'is_published']
    search_fields = ['student__user__username']

@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    list_display = ['title', 'subject', 'class_assigned', 'due_date', 'max_score', 'is_published']
    list_filter = ['is_published', 'due_date']
    search_fields = ['title', 'subject__name']

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(ModelAdmin):
    list_display = ['assignment', 'student', 'submission_date', 'score', 'is_late', 'is_graded']
    list_filter = ['is_late', 'is_graded']
    search_fields = ['assignment__title', 'student__user__username']