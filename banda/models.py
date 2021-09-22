from django.db import models

class Banda(models.Model):
    nombre = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.nombre