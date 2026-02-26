from django.db import models
from PIL import Image
from categoria.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.imagen.path)
        if img.width > 500 or img.height > 500:
            img = img.resize((500, 500))
            img.save(self.imagen.path)

    def __str__(self):
        return self.nombre
