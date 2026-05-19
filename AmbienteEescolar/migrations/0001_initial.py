from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AmbienteCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('titulo_html', models.CharField(blank=True, max_length=120, verbose_name='Título (HTML)')),
                ('descripcion', models.CharField(blank=True, max_length=240, verbose_name='Descripción')),
                ('icono', models.CharField(blank=True, max_length=8, verbose_name='Icono')),
                ('barra', models.CharField(default='linear-gradient(to right, #D0021B, #ff6b6b)', max_length=140, verbose_name='Barra (CSS)')),
                ('publicada', models.BooleanField(default=True, verbose_name='Publicada')),
                ('orden', models.PositiveSmallIntegerField(default=0, verbose_name='Orden de aparición')),
            ],
            options={
                'verbose_name': 'Categoría de Ambiente',
                'verbose_name_plural': 'Categorías de Ambiente',
                'ordering': ['orden', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='AmbienteImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('imagen', models.ImageField(upload_to='ambiente/', verbose_name='Imagen')),
                ('descripcion', models.CharField(blank=True, max_length=200, verbose_name='Descripción corta')),
                ('publicada', models.BooleanField(default=True, verbose_name='Publicada')),
                ('orden', models.PositiveSmallIntegerField(default=0, verbose_name='Orden de aparición')),
                ('fecha_subida', models.DateField(auto_now_add=True, verbose_name='Fecha de subida')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='AmbienteEescolar.ambientecategoria')),
            ],
            options={
                'verbose_name': 'Imagen de Ambiente',
                'verbose_name_plural': 'Imágenes de Ambiente',
                'ordering': ['orden', '-fecha_subida'],
            },
        ),
    ]
