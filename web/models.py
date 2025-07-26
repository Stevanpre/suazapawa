from django.db import models
from django.utils import timezone
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descripcion_corta = models.CharField("Descripción corta", max_length=200)
    descripcion_detallada = models.TextField("Descripción detallada")
    fecha = models.DateField("Fecha del evento")
    hora = models.TimeField("Hora del evento")
    lugar = models.CharField("Lugar", max_length=100)
    imagen = models.ImageField("Imagen del evento", upload_to='calendario')

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descripcion = models.TextField("Descripción")
    fecha = models.DateField("Fecha de publicación")
    hora = models.TimeField("Hora de publicación")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)
    email       = models.EmailField()
    telefono    = models.CharField(max_length=20)
    mensaje     = models.TextField()
    creado_en   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} {self.apellido} — {self.email}"
