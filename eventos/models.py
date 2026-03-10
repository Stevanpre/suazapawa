from django.db import models


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
