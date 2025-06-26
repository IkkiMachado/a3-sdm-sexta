from django.shortcuts import render
from .models import Cliente
from rest_framework import viewsets
from .serializer import ClienteSerializer

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer