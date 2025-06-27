from django.shortcuts import render
from .models import Reserva
from rest_framework import viewsets
from .serializer import ReservaSerializer
# Create your views here.

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer