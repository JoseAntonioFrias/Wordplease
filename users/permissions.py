from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser
