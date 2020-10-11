"""Django  models utilities"""

#Django
from django.db import models

class TiendaModel(models.Model):
    """Modelo base de tienda.

    TiendaModel Actua como una clase base abstracta en la cual cada modelo del proyecto 
    heredará esta clase proporciona cada tabla con los siguientes atributos:
        +created (DateTime): Almacena la fecha y hora en el que se creo el objeto
        +modified (DateTime): Almacena la ultima fecha y hora en que se modifico el objeto    
    """
    created = models.DateTimeField(
        'created at',        
        auto_now_add=True,
        help_text='Fecha y hora en que se creo el objeto.'
    )

    modified = models.DateTimeField(
        'modified at',         
        auto_now=True,
        help_text='Fecha y hora en que se modifico por ultima vez el objeto.'
    )

    class Meta:
        """Meta option."""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
