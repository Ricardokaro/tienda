""" Purchase model. """
#django
from django.db import models

#utilitis
from tienda.utils.models import TiendaModel

class Purchase(TiendaModel):
    """Purshe model.
    """
    client = models.ForeignKey('users.User', on_delete=models.CASCADE)

    products = models.ManyToManyField(
        'stores.Product',
        through = 'stores.PurchaseDetail',
        through_fields = ('purchase', 'product')
    )

    total = models.PositiveIntegerField(default=0, null=True)





