
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import PurchaseDetail

#Serializer
from tienda.stores.serializers import (
    ProductModelSerializer,
    ProductClientModelSerializer, 
    PurchaseModelSerializer, 
    PurchaseStoreModelSerializer,
    PurchaseClientModelSerializer
) 

class PurchaseDetailModelSerializer(serializers.ModelSerializer):
    """
    model serializer
    """
    product = ProductModelSerializer(read_only=True) 
    purchase = PurchaseStoreModelSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = PurchaseDetail
        fields = (
            'id',
            'purchase',
            'product',
            'unit_value',
            'quantity'
        )

class PurchaseDetailClientModelSerializer(serializers.ModelSerializer):
    """
    model serializer
    """
    product = ProductClientModelSerializer(read_only=True) 
    purchase = PurchaseClientModelSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = PurchaseDetail
        fields = (
            'id',
            'purchase',
            'product',
            'unit_value',
            'quantity'
        )