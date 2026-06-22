from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.grading import CAConfiguration

@admin.register(CAConfiguration)
class CAConfigurationAdmin(ModelAdmin):
    list_display = ['subject', 'class_level', 'term', 'ca_weight', 'exam_weight']
    list_filter = ['class_level', 'term']
    search_fields = ['subject__name']