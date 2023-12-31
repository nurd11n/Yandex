from rest_framework.permissions import BasePermission


class IsUserProfile(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_user)


class IsDriverProfile(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_driver)