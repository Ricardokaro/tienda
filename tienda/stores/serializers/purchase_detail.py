
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import PurchaseDetail

#Serializer
from tienda.stores.serializers import (
    ProductModelSerializer,
    ProductClientModelSerializer
)

class PurchaseDetailModelSerializer(serializers.ModelSerializer):

    product = ProductModelSerializer(read_only=True)

    class Meta:

        model = PurchaseDetail
        fields = (
            'product',
            'unit_value',
            'quantity'
        )

class PurchaseDetailClientModelSerializer(serializers.ModelSerializer):

    product = ProductClientModelSerializer(read_only=True)

    class Meta:

        model = PurchaseDetail
        fields = (
            'product',
            'unit_value',
            'quantity'
        )
