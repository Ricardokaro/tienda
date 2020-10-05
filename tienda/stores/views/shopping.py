"""Circle membership views."""

#Django REST Framework
from rest_framework import mixins,status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#Models
from tienda.stores.models import Store, Product, Purchase
from tienda.categories.models import Category

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.stores.permissions import (
    IsOwner,    
    IsClient
) 

#Serializers
from tienda.stores.serializers import (  
    PurchaseModelSerializer    
)

class ClientPurchaseViewSet(mixins.ListModelMixin,                       
                        mixins.RetrieveModelMixin,                                             
                        viewsets.GenericViewSet):
  
    
    serializer_class = PurchaseModelSerializer
    
    def dispatch(self, request, *args, **kwargs):
        return super(ClientPurchaseViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        permissions = [IsAuthenticated]      
        if self.action in ['list']:
            permissions.append(IsClient)        
        return [p() for p in permissions]    
                        
    def get_queryset(self):                
        return Purchase.objects.filter(client=self.client)

    def get_object(self):
        return get_object_or_404( 
            Purchase,
            client = self.client                  
        )

    def perform_destroy(self, instance):      
        instance.is_active = False
        instance.save()   
  

    

