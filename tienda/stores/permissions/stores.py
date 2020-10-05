#Django REST Framework
from rest_framework.permissions import BasePermission

#Models 
from tienda.stores.models import Store

class IsOwner(BasePermission):    
    
    def has_permission(self, request, view):
        obj = view.owner       
        return self.has_object_permission(request,view,obj)
        
    def has_object_permission(self, request, view, obj):
        return request.user == obj

class IsClient(BasePermission):    
  
    def has_permission(self, request, view):
        view.client = request.user        
        if request.user.is_client == True:
            return True
        return False    
        
        
  