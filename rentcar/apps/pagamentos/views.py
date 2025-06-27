from django.shortcuts import render
from .models import Pagamento
from rest_framework import viewsets
from .serializer import PagamentoSerializer

# Create your views here.
class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer