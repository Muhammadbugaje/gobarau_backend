from rest_framework.permissions import BasePermission
from core.choices import RoleChoices


class IsSchoolNurse(BasePermission):
    """Allows access only to users with role 'nurse' or admin-level roles."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
            RoleChoices.NURSE,
        ]

class IsCounsellor(BasePermission):
    """Allows access only to users with role 'counsellor' or admin-level roles."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in [
            RoleChoices.SUPER_ADMIN,
            RoleChoices.PRINCIPAL,
            RoleChoices.VICE_PRINCIPAL,
            RoleChoices.COUNSELLOR,
        ]