from django.db import models

class Flor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cantidad = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='flores/', null=True, blank=True)

    def __str__(self):
        return self.nombre