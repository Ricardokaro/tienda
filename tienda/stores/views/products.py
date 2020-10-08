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
    IsClient,
    IsOwnerOrClient
) 

#Serializers
from tienda.stores.serializers import (
    ProductModelSerializer, 
    AddProductSerializer,
    PurchaseModelSerializer,
    AddPurchaseSerializer
)

class ProductViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
   
    
    serializer_class = ProductModelSerializer
    
    def dispatch(self, request, *args, **kwargs):
        store_name = kwargs['store_name']
        category_name = kwargs['category_name']
        self.category = get_object_or_404(Category, name=category_name)
        self.store = get_object_or_404(Store, name=store_name)
        self.owner = self.store.owner
        return super(ProductViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):        
        print(self.action)
        """Assign permissions based on action."""        
        permissions = [IsAuthenticated]
        if self.action == 'create':            
            permissions.append(IsOwner)
        if self.action in ['partial_update', 'update']:
            permissions.append(IsOwner)        
        return [p() for p in permissions]    
                        
    def get_queryset(self):          
        return Product.objects.filter(
            store=self.store,
            category=self.category,
            is_active=True
        )
        
    def get_object(self):         
        """Retorno detalle producto"""
        return get_object_or_404( 
            Product,
            code = self.kwargs['pk'],
            store__name = self.kwargs['store_name'],
            category__name = self.kwargs['category_name'],
            is_active=True            
        )

    def perform_destroy(self, instance):         
        purchase = Purchase.objects.filter(product__codigo = instance.codigo)        
        if not purchase.exists():          
            instance.is_active = False
            instance.save()   
        
         
  

    def create(self, request, *args, **kwargs):
        
        serializer = AddProductSerializer(
            data=request.data,
            context={'store':self.store, 'category':self.category,'request':request}
        )
        serializer.is_valid(raise_exception=True)
        product = serializer.save()       

        data=self.get_serializer(product).data
        return Response(data,status=status.HTTP_201_CREATED)

 

class AllProductViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,                        
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,                        
                        viewsets.GenericViewSet):
   
    
    serializer_class = ProductModelSerializer
    
    def dispatch(self, request, *args, **kwargs):
        return super(AllProductViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action == 'list':
            permissions.append(IsOwnerOrClient)
        if self.action == 'create':
            permissions.append(IsOwner)
        if self.action == 'shopping':
            permissions.append(IsClient)
                       
        return [p() for p in permissions]    
                        
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
        return get_object_or_404( 
            Product,
            code = self.kwargs['pk']
        )
    
    def create(self, request, *args, **kwargs):

        serializer = AddProductSerializer(
            data=request.data,
            context={'user':request.user}            
        )
        serializer.is_valid(raise_exception=True)
        product = serializer.save()       

        data=self.get_serializer(product).data
        return Response(data,status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def shopping(self, request, *args, **kwargs):
        product = self.get_object()
        store = product.store
        client = request.user

        serializer = AddPurchaseSerializer(          
            data=request.data,
            context={'store':store,'product': product, 'client':client},
            partial = True
        )          

        serializer.is_valid(raise_exception=True)
        purchase = serializer.save()        
        data = PurchaseModelSerializer(purchase).data
        return Response(data, status=status.HTTP_200_OK)    
   

    
