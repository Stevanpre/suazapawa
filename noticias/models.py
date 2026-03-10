from django.db import models



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
