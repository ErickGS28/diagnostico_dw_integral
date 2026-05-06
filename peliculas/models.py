from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    duracion_minutos = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.anio})"

    class Meta:
        ordering = ['-anio']
