from django.db import models

class Flor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='flores/', null=True, blank=True)

    def __str__(self):
        return self.nombre