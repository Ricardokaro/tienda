"""Circle views."""

#Django REST framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.stores.permissions import IsOwner 

#Serializers
from tienda.stores.serializers import PurchaseModelSerializer

#Models
from tienda.stores.models import Store, Product, Purchase

class SaleViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):

        
     serializer_class = PurchaseModelSerializer

     def dispatch(self, request, *args, **kwargs):
        store_name = kwargs['store_name']      
        self.store = get_object_or_404(Store, name=store_name)
        self.owner = self.store.owner
        return super(SaleViewSet, self).dispatch(request, *args, **kwargs)    

     def get_queryset(self):
         queryset = Purchase.objects.filter(store=self.store)
         if self.action == 'list':
             return queryset
         return queryset

     def get_permissions(self):
         permissions = [IsAuthenticated]
         if self.action == 'list':
             permissions.append(IsOwner)         
         return [permission() for permission in permissions]          
    
     