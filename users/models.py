from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('films', 'Films'),
        ('people', 'People'),
        ('locations', 'Locations'),
        ('species', 'Species'),
        ('vehicles', 'Vehicles'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)

    # Definir relaciones Many-to-Many con los grupos y permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    #def save(self, *args, **kwargs):
    #    # Hashear la contraseña si es nueva o ha sido cambiada
    #    if not self.pk or self._state.adding or self.password != self._password:
    #        self.password = make_password(self.password)
    #    super().save(*args, **kwargs)

    def __str__(self):
        return self.username
