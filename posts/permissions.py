from django.utils import timezone
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        return view.action in ('list', 'retrieve') or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (obj.pub_date <= timezone.now() and view.action == 'retrieve') or obj.owner == request.user or request.\
            user.is_superuser
