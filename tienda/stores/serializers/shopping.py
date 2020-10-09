

#Django 
from django.utils import timezone
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Purchase

#serializers
from tienda.categories.serializers import CategoryModelSerializer

from tienda.stores.serializers import (
    StoreModelSerializer, 
    ProductModelSerializer    
)

from tienda.users.serializers import UserModelSerializer

class PurchaseModelSerializer(serializers.ModelSerializer):    
    """
    Purchase model serializer
    """   
    
    client = UserModelSerializer(read_only=True)    
    total = serializers.IntegerField(default=0)

    purchase_date = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Purchase
        fields = (
            'client',            
            'total',
            'purchase_date'            
        )

