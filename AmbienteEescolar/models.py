from django.db import models


class AmbienteCategoria(models.Model):
    nombre = models.CharField("Nombre", max_length=80)
    titulo_html = models.CharField("Título (HTML)", max_length=120, blank=True)
    descripcion = models.CharField("Descripción", max_length=240, blank=True)
    icono = models.CharField("Icono", max_length=8, blank=True)
    barra = models.CharField("Barra (CSS)", max_length=140, default='linear-gradient(to right, #D0021B, #ff6b6b)')
    publicada = models.BooleanField("Publicada", default=True)
    orden = models.PositiveSmallIntegerField("Orden de aparición", default=0)

    class Meta:
        verbose_name = "Categoría de Ambiente"
        verbose_name_plural = "Categorías de Ambiente"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class AmbienteImagen(models.Model):
    categoria = models.ForeignKey(AmbienteCategoria, on_delete=models.CASCADE, related_name='imagenes')
    titulo = models.CharField("Título", max_length=100)
    imagen = models.ImageField("Imagen", upload_to='ambiente/')
    descripcion = models.CharField("Descripción corta", max_length=200, blank=True)
    publicada = models.BooleanField("Publicada", default=True)
    orden = models.PositiveSmallIntegerField("Orden de aparición", default=0)
    fecha_subida = models.DateField("Fecha de subida", auto_now_add=True)

    class Meta:
        verbose_name = "Imagen de Ambiente"
        verbose_name_plural = "Imágenes de Ambiente"
        ordering = ['orden', '-fecha_subida']

    def __str__(self):
        return f"{self.categoria.nombre} · {self.titulo}"
