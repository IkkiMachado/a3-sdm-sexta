from django.shortcuts import render
from .models import ItemReserva
from rest_framework import viewsets
from .serializer import  ItemReservaSerializer
# Create your views here.

class ItemReservaViewSet(viewsets.ModelViewSet):
    queryset = ItemReserva.objects.all()
    serializer_class = ItemReservaSerializer