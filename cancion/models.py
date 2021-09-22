from django.db import models
from album.models import Album
from banda.models import Banda
from artista.models import Artista
from genero.models import Genero
from subgenero.models import Subgenero
from label.models import Label
from instrumento.models import Instrumento

class Cancion(models.Model):
    nombre = models.CharField(max_length=500)
    fecha = models.DateField()
    id_externo = models.CharField(max_length=4)
    duracion = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    subgenero = models.ForeignKey(Subgenero, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre


class CancionBanda(models.Model):
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE, related_name='cancion_banda')
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='banda')


class CancionLabel(models.Model):
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE, related_name='cancion_label')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='label')


class CancionInstrumento(models.Model):
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE, related_name='cancion_instrumento')
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, related_name='instrumento')