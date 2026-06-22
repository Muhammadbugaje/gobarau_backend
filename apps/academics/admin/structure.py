from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.academics.models.structure import Class

@admin.register(Class)
class ClassAdmin(ModelAdmin):
    list_display = ['name', 'class_level', 'wing', 'session', 'capacity', 'is_active']
    list_filter = ['class_level', 'wing', 'session', 'is_active']
    search_fields = ['name']