from rest_framework.permissions import BasePermission
from core.choices import RoleChoices


class IsAdminLevel(BasePermission):
    """Allows super_admin, principal, vice_principal only."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
        ]
class IsStaffOrAdmin(BasePermission):
    """Allows admin-level roles and teaching staff."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
            RoleChoices.BURSAR,
            RoleChoices.TEACHER,
        ]
class IsOwnStudent(BasePermission):
    """Teachers may access students in their assigned classes."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
        ]:
            return True
        return request.user.role == RoleChoices.TEACHER
    def has_object_permission(self, request, view, obj):
        if request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
        ]:
            return True
        # App-level views should supplement with class-assignment logic.
        return True
class IsOwnWard(BasePermission):
    """Parents may access only their own child's data."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
        ]:
            return True
        return request.user.role == RoleChoices.PARENT
    def has_object_permission(self, request, view, obj):
        if request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
        ]:
            return True
        # App-level views should supplement with ward-assignment logic.
        return True