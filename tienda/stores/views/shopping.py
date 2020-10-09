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
    IsClient
) 

#Serializers
from tienda.stores.serializers import (  
    PurchaseModelSerializer,
    AddPurchaseSerializer,    
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
  

class ShoppingViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,                                                   
                      viewsets.GenericViewSet): 

    serializer_class = PurchaseModelSerializer   
    
    def create(self, request, *args, **kwargs):       
        
        client = request.user
        products = request.data['products']
        request.data.pop('products')

        #creamos la compra
        purchase = Purchase.objects.create(
            client=client                      
        )
        purchase.save()

       
        for product in products:            
            prod = Product.objects.get(id=product['id'])

            #guardamos detalle de compra
            purchase_detail = PurchaseDetail.objects.create(
                product = prod,
                purchase = purchase,
                unit_value = prod.price,
                quantity = product['quantity']                 
            )
            purchase_detail.save()

            prod.stock -= product['quantity']
            prod.save()

            purchase.total += product['quantity'] * prod.price

        purchase.save()

        data = self.get_serializer(purchase).data
        return Response(data,status=status.HTTP_201_CREATED)

    

