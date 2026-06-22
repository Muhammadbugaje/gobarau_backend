from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import Person, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "wing", "is_active", "is_verified")
    list_filter = ("role", "wing", "is_active", "is_verified")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)
    fieldsets = UserAdmin.fieldsets + (
        ("School Information", {
            "fields": ("role", "wing", "is_verified", "preferences"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("School Information", {
            "fields": ("role", "wing", "is_verified", "preferences"),
        }),
    )
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "gender", "phone_primary", "user", "is_archived")
    list_filter = ("gender", "is_archived", "state_of_origin")
    search_fields = ("first_name", "last_name", "middle_name", "phone_primary", "email_personal")
    ordering = ("last_name", "first_name")
    readonly_fields = (
        "public_id", "created_at", "updated_at", "created_by", "updated_by",
        "is_archived", "archived_at", "archived_by",
    )
    fieldsets = (
        ("Personal Information", {
            "fields": ("user", "first_name", "last_name", "middle_name", "preferred_name", "date_of_birth", "gender", "photo")
        }),
        ("Contact", {
            "fields": ("phone_primary", "phone_secondary", "email_personal", "address")
        }),
        ("Origin & Identity", {
            "fields": ("state_of_origin", "lga", "religion", "nationality", "national_id", "external_ref", "language")
        }),
        ("Metadata", {
            "fields": ("metadata",),
            "classes": ("collapse",),
        }),
        ("System", {
            "fields": ("public_id", "is_archived", "archived_at", "archived_by", "created_at", "updated_at", "created_by", "updated_by"),
            "classes": ("collapse",),
        }),
    )
    def get_queryset(self, request):
        return self.model.all_objects.all()