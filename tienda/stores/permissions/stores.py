#Django REST Framework
from rest_framework.permissions import BasePermission

#Models 
from tienda.stores.models import Store

class IsOwnerOrClient(BasePermission):
    def has_permission(self, request, view):
        #import pdb ; pdb.set_trace()        
        return request.user.is_admin or request.user.is_client

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        #import pdb ; pdb.set_trace()        
        return request.user.is_admin 

class IsClient(BasePermission):
    def has_permission(self, request, view):
        #import pdb ; pdb.set_trace()        
        return request.user.is_client


            
        
        
  