#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#Utilities
from tienda.utils.models import TiendaModel

class User(TiendaModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
       'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exits.'
        }
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Ayuda a distinguir facilmente a los usuarios y realizar consultas. '            
        )
    )

    is_admin = models.BooleanField(
        'admin',
        default=False,
        help_text=(
            'El usuario administrador es el dueño de la tienda.'            
        )
    )   


    def __str__(self):        
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username"""
        return self.username    
    
