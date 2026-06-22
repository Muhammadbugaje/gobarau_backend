from django.contrib import admin
from apps.administration.models import (
    AcademicSession, Campus, ClassLevel, Department,
    GradingBand, GradingScale, SchoolSettings, Term, Wing
)


@admin.register(SchoolSettings)
class SchoolSettingsAdmin(admin.ModelAdmin):
    list_display = ("name", "motto", "email", "phone", "academic_year")
    search_fields = ("name", "email", "phone")
@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "is_current")
    list_filter = ("is_current",)
    search_fields = ("name",)
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "session", "start_date", "end_date", "is_current")
    list_filter = ("name", "is_current", "session")
    search_fields = ("name", "session__name")
@admin.register(Wing)
class WingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "color_code", "description")
    list_filter = ("name",)
@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "principal", "is_main", "is_active")
    list_filter = ("is_main", "is_active")
    search_fields = ("name", "address", "phone")
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "head")
    search_fields = ("name", "code")
@admin.register(ClassLevel)
class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "order_index", "education_tier")
    list_filter = ("education_tier",)
    search_fields = ("name", "code")
@admin.register(GradingScale)
class GradingScaleAdmin(admin.ModelAdmin):
    list_display = ("name", "session", "is_active")
    list_filter = ("is_active", "session")
    search_fields = ("name",)
@admin.register(GradingBand)
class GradingBandAdmin(admin.ModelAdmin):
    list_display = ("__str__", "grading_scale", "min_score", "max_score", "grade", "grade_point", "remark")
    list_filter = ("grading_scale",)
    search_fields = ("grade", "remark")