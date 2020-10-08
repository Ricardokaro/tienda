""" Product model. """
#django 
from django.db import models

#utilitis
from tienda.utils.models import TiendaModel

class Product(TiendaModel):
 
    
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=140)
    
     
    price = models.PositiveIntegerField(default=0) 
    stock = models.PositiveIntegerField(default=0)
    stock_limited = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category',null=True, on_delete=models.CASCADE)

          

    def __str__(self):
        """Return circle name"""
        return self.name

   
