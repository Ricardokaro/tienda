"""Categories permission classes."""

#Django REST Framework
from rest_framework.permissions import BasePermission

#Models 
from tienda.users.models import User

class IsSuperUser(BasePermission):
    

    def has_object_permission(self, request, view, obj):
        return True    