
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import PurchaseDetail

#Serializer
from tienda.users.serializers import UserModelSerializer

class PurchaseDetailModelSerializer(serializers.ModelSerializer):
    """
    model serializer
    """

    class Meta:
        """
        Meta class
        """
        model = PurchaseDetail
        fields = (
            'unit_value',
            'quantity'
        )