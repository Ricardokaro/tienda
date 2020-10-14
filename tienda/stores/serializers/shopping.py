#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Purchase

from tienda.users.serializers import UserModelSerializer, UserModelClientSerializer

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


class PurchaseStoreModelSerializer(serializers.ModelSerializer):
    """
    Purchase model serializer
    """

    client = UserModelSerializer(read_only=True)
    purchase_date = serializers.DateTimeField(source='created', read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Purchase
        fields = (
            'id',
            'client',
            'purchase_date'
        )


class PruebaPurchaseClientModelSerializer(serializers.ModelSerializer):
    """
    Purchase model serializer
    """

    client = UserModelClientSerializer(read_only=True)
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


