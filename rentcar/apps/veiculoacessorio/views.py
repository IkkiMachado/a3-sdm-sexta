from django.shortcuts import render
from .models import VeiculoAcessorio
from rest_framework import viewsets
from .serializer import VeiculoacessorioSerializer

# Create your views here.
class VeiculoAcessorioViewSet(viewsets.ModelViewSet):
    queryset = VeiculoAcessorio.objects.all()
    serializer_class = VeiculoacessorioSerializer 