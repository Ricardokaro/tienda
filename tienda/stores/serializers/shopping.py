

#Django 
from django.utils import timezone
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Purchase

#serializers
from tienda.categories.serializers import CategoryModelSerializer
from tienda.stores.serializers import StoreModelSerializer, ProductModelSerializer, Store
from tienda.users.serializers import UserModelSerializer

class PurchaseModelSerializer(serializers.ModelSerializer):
    """
    Purchase model serializer
    """
    store = StoreModelSerializer(read_only=True)
    product = ProductModelSerializer(read_only=True)
    client = UserModelSerializer(read_only=True)   

    quantity = serializers.IntegerField(default=0) 
    total = serializers.IntegerField(default=0)

    purchase_date = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Purchase
        fields = (
            'store',           
            'product',
            'client',
            'quantity',
            'total',
            'purchase_date'            
        )

class AddPurchaseSerializer(serializers.Serializer):
    """AddPurchaseSerializer"""
    
    quantity = serializers.IntegerField(default=0)    

    def create(self, data):
        
        """Crear producto"""
        store = self.context['store']      
        product = self.context['product']
        client = self.context['client']
        total = product.price * data['quantity']            
        
        #Purchase creation 
        purchase = Purchase.objects.create(
            **data,
            store=store,            
            product=product,
            client=client,
            total=total              
        )

        #Product
        product.stock -= data['quantity']
        product.save()   
        
        return purchase