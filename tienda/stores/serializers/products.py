#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Product, Store
from tienda.categories.models import Category

#serializers
from tienda.categories.serializers import CategoryModelSerializer
from tienda.stores.serializers import StoreModelSerializer, StoreModelClientSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    """
    model serializer
    """
    category = CategoryModelSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(), source='category')
    store = StoreModelSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Product
        fields = (
            'id',
            'code',
            'name',
            'description',
            'price',
            'stock',
            'stock_limited',
            'category',
            'category_id',
            'store'
        )
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        if instance.stock_limited < validated_data.get('stock', 0):
            raise serializers.ValidationError('Stock sobre pasa el limited')
        return super().update(instance, validated_data)

    def validate_code(self, data):
        """Verificamos si el producto existe."""
        product = Product.objects.filter(code=data, is_active=True)
        if product.exists():
            raise serializers.ValidationError('Producto ya existe.')
        return data

    def validate(self, data):
        """Varifica que el stock limited sea mayor que el stock inicial."""
        if data.get('stock',0) > data.get('stock_limited',0):
            raise serializers.ValidationError('El stock limited debe ser mayor que el stock inicial')
        return data

    def create(self, data):
        """Crear producto"""
        user = self.context['request'].user
        store = Store.objects.get(user=user)
        product = Product.objects.create(
            **data,
            store=store
        )
        return product



class ProductClientModelSerializer(serializers.ModelSerializer):
    """
    model serializer
    """
    category = CategoryModelSerializer(read_only=False)
    store = StoreModelClientSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Product
        fields = (
            'id',
            'code',
            'name',
            'description',
            'price',
            'category',
            'store'
        )









