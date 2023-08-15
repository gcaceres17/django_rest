from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=150)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    

class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    active = models.BooleanField(default=True)
    avg_calificacion = models.FloatField(default=0)
    number_calificacion = models.IntegerField(default=0)
    empresa = models.ForeignKey(Empresa, on_delete= models.CASCADE, related_name="edificacionlist")
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.direccion
    
class Comentarios(models.Model):
    comentario_user = models.ForeignKey(User, on_delete= models.CASCADE)
    calificacion = models.PositiveIntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)])
    texto = models.TextField(blank=True)
    edificacion = models.ForeignKey(Edificacion, on_delete= models.CASCADE, related_name= "comentariolist")
    active = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Calificacion: " + str(self.calificacion) + " - " + self.edificacion.direccion
    