# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=9)
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    fecha_nac = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}  -  {self.cargo}"
