from rest_framework import serializers
from cancion.models import Cancion


class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ('id',
                  'nombre')