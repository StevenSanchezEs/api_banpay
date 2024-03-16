from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import CustomUser


class CanAccessGhibliEndpoint(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Mapear los endpoints permitidos con los roles asociados
        allowed_endpoints = {
            'films': ['films', 'admin'],
            'people': ['people', 'admin'],
            'locations': ['locations', 'admin'],
            'species': ['species', 'admin'],
            'vehicles': ['vehicles', 'admin']
        }

        # Obtener el endpoint solicitado desde la vista
        endpoint = getattr(view, 'endpoint', None)
        if endpoint is None:
            return False
        
        # Verificar si el usuario tiene permiso para acceder al endpoint
        user_roles = request.user.rol.split(',') if request.user.rol else []
        for role in user_roles:
            if role.strip() in allowed_endpoints.get(endpoint, []):
                return True
        
        # Permitir acceso al superusuario
        if request.user.is_superuser:
            return True
        
        return False


class AdminPermission(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los superadmins y a los usuarios con rol de admin realizar operaciones CRUD
    en el endpoint de usuarios.
    """

    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            return False

        # Verificar si el usuario es superadmin
        if request.user.is_superuser:
            return True

        # Verificar si el usuario tiene un rol de admin
        if request.user.rol == 'admin':
            # Verificar que el método de la vista sea de lectura (GET) o creación (POST)
            if view.action in ['list', 'create', 'retrieve']:
                return True
            # Para los métodos de actualización (PUT, PATCH) y eliminación (DELETE), verificar si el usuario
            # es un superadmin o un admin, pero no está intentando eliminar a otro admin o al superadmin
            elif view.action in ['update', 'partial_update', 'destroy']:
                if 'pk' in view.kwargs:
                    user_id = view.kwargs['pk']
                    user = CustomUser.objects.get(pk=user_id)
                    return not (user.is_superuser or (user.rol == 'admin' and not request.user.is_superuser))
            # Otros métodos no permitidos
            return False

        # Otros usuarios no tienen permiso
        return False

