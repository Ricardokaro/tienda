#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Purchase, Store

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

    def to_representation(self, instance):
        representention = super(PurchaseStoreModelSerializer, self).to_representation(instance)
        owner = self.context['request'].user
        store = Store.objects.filter(product__store__owner=owner)[0]
        purchase_detail = instance.purchasedetail_set.filter(product__store=store)
        detalle_serializer = PurchaseDetailClientModelSerializer(purchase_detail,many=True)
        representention['detail'] = detalle_serializer.data
        representention['total'] = 0
        for detail in purchase_detail:
            representention['total'] += detail.quantity * detail.unit_value
        return representention


