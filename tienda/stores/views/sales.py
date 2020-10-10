"""Circle views."""

#Django REST framework
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.stores.permissions import IsOwner 

#Serializers
from tienda.stores.serializers import PurchaseModelSerializer, PurchaseDetailModelSerializer

#Models
from tienda.stores.models import Store, Product, Purchase, PurchaseDetail

class SaleViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
        
     serializer_class = PurchaseDetailModelSerializer

     def dispatch(self, request, *args, **kwargs):       
        return super(SaleViewSet, self).dispatch(request, *args, **kwargs)    

     def get_queryset(self):
         queryset = PurchaseDetail.objects.filter(product__store__owner = self.request.user)
         return PurchaseDetail.objects.all()
           

     def get_permissions(self):
         permissions = [IsAuthenticated]
         if self.action == 'list':
             permissions.append(IsOwner)         
         return [permission() for permission in permissions]          
    
     