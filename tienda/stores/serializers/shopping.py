#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Purchase

from tienda.users.serializers import UserModelSerializer, UserModelClientSerializer

#Serializer
from tienda.stores.serializers import PurchaseDetailClientModelSerializer

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
            'id',
            'client',
            'total',
            'purchase_date'
        )

class PurchaseClientModelSerializer(serializers.ModelSerializer):
    """
    Purchase model serializer
    """

    client = UserModelClientSerializer(read_only=True)
    detail = PurchaseDetailClientModelSerializer(read_only=True, many=True,  source='purchasedetail_set')
    total = serializers.IntegerField(default=0)
    purchase_date = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Purchase
        fields = (
            'id',
            'client',
            'detail',
            'total',
            'purchase_date'
        )

        read_only_fields = ('detail',)


class PurchaseStoreModelSerializer(serializers.ModelSerializer):
    """
    Purchase model serializer
    """

    client = UserModelSerializer(read_only=True)
    detail = PurchaseDetailClientModelSerializer(read_only=True, many=True,  source='purchasedetail_set')
    purchase_date = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Purchase
        fields = (
            'id',
            'client',
            'detail',
            'purchase_date'
        )


