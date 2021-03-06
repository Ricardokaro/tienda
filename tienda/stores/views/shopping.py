"""Circle membership views."""

#Django
from django.db import transaction

#Django REST Framework
from rest_framework import mixins,status, viewsets
from rest_framework.response import Response

#Models
from tienda.stores.models import  Product, Purchase, PurchaseDetail

#Permissions
from rest_framework.permissions import IsAuthenticated
from tienda.stores.permissions import (
    IsClient
)

#Serializers
from tienda.stores.serializers import (
    PurchaseClientModelSerializer
)

class ShoppingViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['list', 'create']:
            permissions.append(IsClient)
        return [p() for p in permissions]

    def get_queryset(self):
        return Purchase.objects.filter(client = self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return PurchaseClientModelSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):

        client = request.user
        products = request.data['products']
        request.data.pop('products')

        #creamos la compra
        purchase = Purchase.objects.create(
            client=client
        )

        for product in products:
            prod = Product.objects.get(id=product['id'])
            #guarda detalle de compra
            PurchaseDetail.objects.create(
                product = prod,
                purchase = purchase,
                unit_value = prod.price,
                quantity = product['quantity']
            )
            prod.stock -= product['quantity']
            prod.save()
            purchase.total += product['quantity'] * prod.price
        purchase.save()
        data = self.get_serializer(purchase).data
        return Response(data,status=status.HTTP_201_CREATED)









