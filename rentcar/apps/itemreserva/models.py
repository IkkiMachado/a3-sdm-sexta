from django.db import models
from django.core.validators import MinValueValidator
from datetime import date
from veiculos.models import Veiculo
from reservas.models import Reserva

class ItemReserva(models.Model):
    reserva = models.ForeignKey(
        Reserva, 
        on_delete=models.CASCADE,
        related_name='itens'
    )
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.PROTECT,
        related_name='itemreserva'
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_diaria = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    valor_parcial = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"Item #{self.id} - {self.veiculo} ({self.data_inicio} a {self.data_fim})"

    def calcular_valor_parcial(self):
        """Calcula o valor parcial com base nos dias e acessórios"""
        dias = (self.data_fim - self.data_inicio).days + 1
        valor_acessorios = sum(
            item.acessorio.preco_adicional * dias * item.quantidade
            for item in self.itens_acessorios.all()
        )
        return (self.valor_diaria * dias) + valor_acessorios

    def save(self, *args, **kwargs):
        """Atualiza automaticamente o valor_parcial ao salvar"""
        if not self.valor_parcial or self.pk is None:
            self.valor_parcial = self.calcular_valor_parcial()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "itemreserva"
        verbose_name_plural = "itemreserva"
        ordering = ['data_inicio']