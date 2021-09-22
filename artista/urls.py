from django.urls import path
from .views import *

urlpatterns = [
    path('api/artistas', artistas_lista),
    path('api/artistas/<int:pk>', artistas_detalle),
]