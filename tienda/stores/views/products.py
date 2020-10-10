"""Circle membership views."""

#Django REST Framework
from rest_framework import mixins,status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#Models
from tienda.stores.models import Store, Product, Purchase, PurchaseDetail
from tienda.categories.models import Category

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.stores.permissions import (
    IsOwner,    
    IsClient,
    IsOwnerOrClient
) 

#Serializers
from tienda.stores.serializers import (
    ProductModelSerializer, #
    AddProductSerializer,   #    
    ProductClientModelSerializer    
)  

class AllProductViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,                        
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin,                        
                        viewsets.GenericViewSet):
    
    def dispatch(self, request, *args, **kwargs):
        return super(AllProductViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action == 'list':
            permissions.append(IsOwnerOrClient)
        if self.action in ['create', 'destroy']:
            permissions.append(IsOwner)
        return [p() for p in permissions]

    def get_serializer_class(self):
        """Retorna serializer en base al rol del usuario."""        
        if self.request.user.is_admin:
            return  ProductModelSerializer
        if self.request.user.is_client:
            #import pdb ; pdb.set_trace()
            return ProductClientModelSerializer
                        
    def get_queryset(self):       
        if self.action == 'list':            
            if self.request.user.is_admin:
                store = Store.objects.get(user=self.request.user)
                #import pdb ; pdb.set_trace()                 
                products = Product.objects.filter(           
                    stock__gt = 0,
                    is_active=True,
                    store = store
                )      
            if self.request.user.is_client:
                 products = Product.objects.filter(           
                    stock__gt = 0,
                    is_active=True                   
                )
            return products

    def get_object(self):         
        """Retorno detalle producto"""
        #import pdb ; pdb.set_trace()   
        return get_object_or_404( 
            Product,
            pk = self.kwargs['pk']
        )
    
    def create(self, request, *args, **kwargs):
        #import pdb ; pdb.set_trace() 
        serializer = AddProductSerializer(
            data=request.data,
            context={'user':request.user}            
        )
        serializer.is_valid(raise_exception=True)
        product = serializer.save()       

        data=self.get_serializer(product).data
        return Response(data,status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        if not PurchaseDetail.objects.filter(product=instance).exists():
            instance.delete()            
        #import pdb ; pdb.set_trace() 
    
   
class AllProductStoreViewSet(mixins.ListModelMixin,                                                   
                             viewsets.GenericViewSet):

    serializer_class = ProductClientModelSerializer
    
    def dispatch(self, request, *args, **kwargs):            
        #import pdb ; pdb.set_trace() 
        self.store = get_object_or_404( 
            Store,
            pk = kwargs['store_id']
        )           
        return super(AllProductStoreViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action == 'list':
            permissions.append(IsClient)
        return [p() for p in permissions]   
                        
    def get_queryset(self):
        #import pdb ; pdb.set_trace() 
        return Product.objects.filter(           
            stock__gt = 0,
            is_active = True,
            store = self.store
        )


        
            

   
    
