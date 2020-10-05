

#Django 
from django.utils import timezone
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Product, Store
from tienda.categories.models import Category

#serializers
from tienda.categories.serializers import CategoryModelSerializer
from tienda.stores.serializers import StoreModelSerializer

class ProductModelSerializer(serializers.ModelSerializer):
    """
    model serializer
    """
    category = CategoryModelSerializer(read_only=False)
    store = StoreModelSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Product
        fields = (           
            'codigo',
            'name',
            'description',
            'price',
            'stock',
            'stock_limited',
            'category',
            'store'
        )

    def update(self, instance, validated_data):        
        if instance.stock_limited < validated_data.get('stock', 0):
            raise serializers.ValidationError('Stock sobre pasa el limited')
        return super().update(instance, validated_data)


class AddProductSerializer(serializers.Serializer):
    
    
    codigo = serializers.CharField(max_length=10)
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(max_length=40)
    description = serializers.CharField(max_length=140)     
    price = serializers.IntegerField(default=0) 
    stock = serializers.IntegerField(default=0)
    stock_limited = serializers.IntegerField(default=0)    

    def validate_codigo(self, data):       
        """Verificamos si el producto existe"""
        store = self.context['store']
        product = Product.objects.filter(codigo=data, store=store, is_active=True)
        if product.exists():
            raise serializers.ValidationError('Producto ya existe.')
        return data
       

    
    def validate(self, data):
        """Varificamis que el stock limited sea mayor que el stock inicial ."""       
             
        if data['stock'] >= data['stock_limited']:
            raise serializers.ValidationError('El stock limited debe ser mayor que el stock inicial')        
        return data

    def create(self, data):
        """Crear producto"""      
        store = self.context['store']
        category = self.context['category']     
        
        #Product creation 
        product = Product.objects.create(
            **data,            
            store=store,
            category=category            
        )
        
        return product