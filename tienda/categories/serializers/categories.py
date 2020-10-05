"""Circle serializers."""
#Django REST Framework
from rest_framework import serializers

#Model
from tienda.categories.models import Category
from tienda.users.models import User


class CategoryModelSerializer(serializers.ModelSerializer):
    """Category model serializer."""

    name = serializers.CharField(max_length=50)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())    

    class Meta:
        """Meta class."""
        model = Category
        fields = (
            'name',
            'user'            
        )

    def validate_user(self, data):            
        
        user = data
        #import pdb ; pdb.set_trace()
        
        q = User.objects.filter(pk=user.pk, is_superuser = True)                 
        if not q.exists():
            raise serializers.ValidationError('No tiene permisos para esta accion')        
        return data

    def validate(self, data):
         
        return data    
       
 