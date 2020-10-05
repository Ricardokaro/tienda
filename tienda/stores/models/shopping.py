""" Purchase model. """
#django 
from django.db import models

#utilitis
from tienda.utils.models import TiendaModel

class Purchase(TiendaModel):
    """Purshe model.    
    """

    store = models.ForeignKey('stores.Store', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey('stores.Product', on_delete=models.CASCADE)
    client = models.ForeignKey('users.User', on_delete=models.CASCADE)    
     
    quantity = models.PositiveIntegerField(default=0) 
    total = models.PositiveIntegerField(default=0)   
          

  

   
