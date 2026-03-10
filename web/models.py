from django.db import models


class ImagenGaleria(models.Model):
    titulo = models.CharField("Título", max_length=100)
    imagen = models.ImageField("Imagen", upload_to='galeria/')
    descripcion = models.CharField("Descripción corta", max_length=200, blank=True)
    publicada = models.BooleanField("Publicada", default=True)
    orden = models.PositiveSmallIntegerField("Orden de aparición", default=0)
    fecha_subida = models.DateField("Fecha de subida", auto_now_add=True)

    class Meta:
        verbose_name = "Imagen de Galería"
        verbose_name_plural = "Imágenes de Galería"
        ordering = ['orden', '-fecha_subida']

    def __str__(self):
        return self.titulo

