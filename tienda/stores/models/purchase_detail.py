""" Purchase model. """
#django 
from django.db import models

#utilitis
from tienda.utils.models import TiendaModel

class PurchaseDetail(TiendaModel):
    """Purshe model.    
    """    
    product = models.ForeignKey('stores.Product', on_delete=models.CASCADE)
    purchase = models.ForeignKey('stores.Purchase', on_delete=models.CASCADE)    

    unit_value = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0) 
    
          