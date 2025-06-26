from django.db import models
from categorias.models import Categoria
# Create your models here.

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
    
    def __str__(self):
        return self.name