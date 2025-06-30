from django.db import models
from clientes.models import Cliente
# Create your models here.

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada')
    ])
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering =['id']

    def __str__(self):
        return f"Reserva #{self.id} - {self.cliente.nome}"