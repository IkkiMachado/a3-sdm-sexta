from django.db import models
from django.core.validators import MinValueValidator
from itemreserva.models import ItemReserva
from acessorios.models import Acessorio

class VeiculoAcessorio(models.Model):
    item_reserva = models.ForeignKey(
        ItemReserva,
        on_delete=models.CASCADE,
        related_name='veiculo_acessorios',
        verbose_name='Item de Reserva'
    )
    acessorio = models.ForeignKey(
        Acessorio,
        on_delete=models.PROTECT,
        related_name='reserva_acessorios',
        verbose_name='Acessório'
    )
    quantidade = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Quantidade'
    )
    preco_adicional = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Preço Adicional (por dia)'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.acessorio.nome} (Item Reserva #{self.item_reserva.id})"

    def save(self, *args, **kwargs):
        """Garante que o preço adicional sempre reflete o preço atual do acessório"""
        if not self.pk or self.preco_adicional != self.acessorio.preco_adicional:
            self.preco_adicional = self.acessorio.preco_adicional
        super().save(*args, **kwargs)

    @property
    def valor_total(self):
        """Calcula o valor total deste acessório para o período de reserva"""
        dias = (self.item_reserva.data_fim - self.item_reserva.data_inicio).days + 1
        return self.preco_adicional * dias * self.quantidade

    class Meta:
        verbose_name = 'Acessório de Veículo (Reserva)'
        verbose_name_plural = 'Acessórios de Veículo (Reserva)'
        unique_together = ('item_reserva', 'acessorio')
