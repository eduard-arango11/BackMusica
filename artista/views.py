from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from artista.models import Artista
from cancion.models import Cancion
from artista.serializers import ArtistaSerializer
from cancion.serializers import CancionSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def artistas_lista(request):
    if request.method == 'GET':
        artistas = Artista.objects.all()

        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            artistas = artistas.filter(nombre__icontains=nombre)

        artistas_serializer = ArtistaSerializer(artistas, many=True)
        return JsonResponse(artistas_serializer.data, safe=False)

    elif request.method == 'POST':
        artista_data = JSONParser().parse(request)
        artista_serializer = ArtistaSerializer(data=artista_data)
        if artista_serializer.is_valid():
            artista_serializer.save()
            return JsonResponse(artista_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(artista_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def artistas_detalle(request, pk):
    try:
        artista = Artista.objects.get(pk=pk)
    except Artista.DoesNotExist:
        return JsonResponse({'message': 'El artista no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        artista_serializer = ArtistaSerializer(artista)
        print("artista_serializer: ", artista_serializer)
        canciones = Cancion.objects.filter(artista=artista)
        print("canciones: ", canciones)
        response = {'nombre':artista.nombre}
        return JsonResponse(response)