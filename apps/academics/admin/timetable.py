from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.timetable import Timetable, ExamTimetable

@admin.register(Timetable)
class TimetableAdmin(ModelAdmin):
    list_display = ['class_assigned', 'subject', 'teacher', 'day', 'start_time', 'end_time']
    list_filter = ['day', 'class_assigned']
    search_fields = ['class_assigned__name', 'subject__name']

@admin.register(ExamTimetable)
class ExamTimetableAdmin(ModelAdmin):
    list_display = ['class_assigned', 'subject', 'term', 'exam_date', 'start_time', 'venue']
    list_filter = ['term', 'exam_date']
    search_fields = ['class_assigned__name', 'subject__name', 'venue']