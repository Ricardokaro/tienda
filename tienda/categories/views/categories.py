"""Circle views."""

#Django REST framework
from rest_framework import viewsets, mixins
from rest_framework import generics

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.categories.permissions import  IsSuperUser

#filters
from rest_framework.filters import SearchFilter, OrderingFilter

#Serializers
from tienda.categories.serializers import CategoryModelSerializer

#Models
from tienda.categories.models import Category

class CategoryViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

     """Category view set."""
     serializer_class = CategoryModelSerializer
     queryset = Category.objects.all()

     # filters
     filter_backends = (SearchFilter, OrderingFilter)
     search_fields = ('name',)
     ordering_filter = ('name',)

     def get_permissions(self):
         permissions = [IsAuthenticated]
         if self.action in ['update', 'partial_update']:
             permissions.append(IsSuperUser)
         return [permission() for permission in permissions]

