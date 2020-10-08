"""Circle serializers."""
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.categories.models import Category
from tienda.users.models import User


class CategoryModelSerializer(serializers.ModelSerializer):
    """Category model serializer."""

    name = serializers.CharField(max_length=50)   

    class Meta:
        """Meta class."""
        model = Category
        fields = (  
            'id',    
            'name'                             
        )
                           
           
        
 