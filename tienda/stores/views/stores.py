"""Circle views."""

#Django REST framework
from rest_framework import viewsets, mixins

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.stores.permissions import IsOwner

#Serializers
from tienda.stores.serializers import StoreModelSerializer

#Models
from tienda.stores.models import Store

class StoreViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):


     serializer_class = StoreModelSerializer

     def get_queryset(self):
         queryset = Store.objects.all()
         if self.action == 'list':
             return queryset
         return queryset

     def get_permissions(self):
         permissions = [IsAuthenticated]
         if self.action in ['update', 'partial_update']:
             permissions.append(IsOwner)
         return [permission() for permission in permissions]

