"""Circle views."""

#Django REST framework
from rest_framework import viewsets, mixins

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.categories.permissions import  IsSuperUser

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
     

     
     def get_queryset(self):        
         queryset = Category.objects.all()          
         return queryset

     def get_permissions(self):
         permissions = [IsAuthenticated]
         if self.action in ['update', 'partial_update']:
             permissions.append(IsSuperUser)         
         return [permission() for permission in permissions]          
    
   