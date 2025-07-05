from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion_corta = models.CharField(max_length=200)
    descripcion_detallada = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='calendario')

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.titulo
