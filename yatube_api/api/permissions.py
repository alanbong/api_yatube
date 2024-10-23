from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешает редактировать и удалять объект только его автору."""

    def has_object_permission(self, request, view, obj):
        # Разрешить методы GET, HEAD, OPTIONS для любого пользователя
        # Разрешить редактирование и удаление только автору объекта
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
