""" Store model. """
#django 
from django.db import models

#utilitis
from tienda.utils.models import TiendaModel

class Store(TiendaModel):
   
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=140)    

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, related_name='owner')

    def __str__(self):
        """Return circle name"""
        return self.name   
    
