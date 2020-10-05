# Django
from django.db import models

# Utilities
from tienda.utils.models import TiendaModel

class Category(TiendaModel):
    
    name = models.CharField(max_length=50)

