
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import PurchaseDetail

#Serializer
from tienda.stores.serializers import (
    ProductModelSerializer,
    PurchaseStoreModelSerializer,
    ProductClientModelSerializer,
    PurchaseClientModelSerializer
)

class PurchaseDetailModelSerializer(serializers.ModelSerializer):

    product = ProductModelSerializer(read_only=True)
    purchase = PurchaseStoreModelSerializer(read_only=True)

    class Meta:

        model = PurchaseDetail
        fields = (
            'purchase',
            'product',
            'unit_value',
            'quantity'
        )

class PurchaseDetailClientModelSerializer(serializers.ModelSerializer):

    product = ProductClientModelSerializer(read_only=True)
    purchase = PurchaseClientModelSerializer(read_only=True)

    class Meta:

        model = PurchaseDetail
        fields = (
            'purchase',
            'product',
            'unit_value',
            'quantity'
        )
