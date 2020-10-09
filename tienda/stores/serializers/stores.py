
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.stores.models import Store

#Serializer
from tienda.users.serializers import UserModelSerializer

class StoreModelClientSerializer(serializers.ModelSerializer):
    """Store model serializer."""
  
    class Meta:
        """Meta class."""
        model = Store
        fields = (
            'id',            
            'name',
            'address'                
        )

class StoreModelSerializer(serializers.ModelSerializer):
    """Store model serializer."""
  

    owner = UserModelSerializer(read_only=True) 
    address = serializers.CharField(max_length=140) 
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  

    class Meta:
        """Meta class."""
        model = Store
        fields = (            
            'id',
            'name',
            'address',
            'user',
            'owner'           
        )
        
    def validate(self, data):        
        return data

    def create(self, data):      
        user = data['user']        
        user.is_admin = True
        user.is_client = False
        user.save()        
        store = Store.objects.create(**data, owner=user)
        return store  