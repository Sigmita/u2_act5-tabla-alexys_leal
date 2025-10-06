from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en minutos")
    director = models.CharField(max_length=100)
    reparto = models.TextField(help_text="Lista de actores principales")
    clasificacion = models.CharField(max_length=10, help_text="Clasificación por edades")
    idioma = models.CharField(max_length=50)
    subtitulos = models.BooleanField(default=False)
    url_trailer = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo