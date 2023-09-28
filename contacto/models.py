from django.db import models

# Create your models here.
class Contacto(models.Model):
    image = models.ImageField(verbose_name="Imagen", upload_to="contacto", null=True, blank=True)
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=100)
    Profesion = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    
    
    
    class Meta:
        verbose_name ="Contacto"
        verbose_name_plural ="Contactos"
    
    def __str__(self):
        return self.Nombre
    
