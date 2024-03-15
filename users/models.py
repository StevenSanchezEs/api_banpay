from django.db import models

# Create your models here.

class Usuario(models.Model):
    ROLES = (
        ('admin', 'Admin'),
        ('films', 'Films'),
        ('people', 'People'),
        ('locations', 'Locations'),
        ('species', 'Species'),
        ('vehicles', 'Vehicles'),
    )
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    
    def __str__(self):
        return self.nombre