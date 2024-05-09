from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешить GET, HEAD, OPTIONS запросы всем

        # Проверить, является ли пользователь администратором
        return request.user.is_superuser
