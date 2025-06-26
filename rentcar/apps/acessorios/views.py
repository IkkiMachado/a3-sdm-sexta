from django.shortcuts import render
from .models import Acessorio
from rest_framework import viewsets
from .serializer import AcessorioSerializer
# Create your views here.

class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer