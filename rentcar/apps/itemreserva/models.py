from django.db import models
from django.core.validators import MinValueValidator
from datetime import date
from veiculos.models import Veiculo
from reservas.models import Reserva

class ItemReserva(models.Model):
    reserva = models.ForeignKey(
        Reserva, 
        on_delete=models.CASCADE,
        related_name='itens_reserva',
        verbose_name='Reserva associada'
    )
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.PROTECT,
        related_name='itens_reserva',
        verbose_name='Veículo reservado'
    )
    data_inicio = models.DateField(
        verbose_name='Data de início',
        help_text='Data de retirada do veículo'
    )
    data_fim = models.DateField(
        verbose_name='Data de término',
        help_text='Data prevista de devolução'
    )
    valor_diaria = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Valor da diária',
        help_text='Valor por dia do veículo'
    )
    valor_parcial = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Valor parcial',
        help_text='Calculado automaticamente (diárias + acessórios)',
        default=0
    )
    observacoes = models.TextField(
        verbose_name='Observações',
        blank=True,
        null=True,
        help_text='Informações adicionais sobre esta reserva'
    )

    def __str__(self):
        return f"Reserva #{self.reserva.id} - {self.veiculo.placa} ({self.data_inicio} a {self.data_fim})"

    def calcular_dias(self):
        """Calcula a quantidade de dias da reserva"""
        return (self.data_fim - self.data_inicio).days + 1

    def save(self, *args, **kwargs):
        """
        Salva o item primeiro para obter um ID,
        depois calcula e atualiza o valor parcial
        """
        super().save(*args, **kwargs)
        
        self.valor_parcial = self.calcular_valor_parcial()
        
        super().save(update_fields=['valor_parcial'])
    
    def calcular_valor_parcial(self):
        """Versão segura que verifica se existe PK"""
        if not self.pk:
            return 0 
            
        valor_diarias = self.valor_diaria * self.calcular_dias()
        valor_acessorios = self.calcular_valor_acessorios()
        return valor_diarias + valor_acessorios
    
    def calcular_valor_acessorios(self):
        """Versão segura que verifica se existe PK"""
        if not self.pk:
            return 0
            
        return sum(
            acessorio.valor_total
            for acessorio in self.veiculo_acessorios.all()
        )
    
    class Meta:
        verbose_name = 'Item de Reserva'
        verbose_name_plural = 'Itens de Reserva'
        ordering = ['data_inicio']
        indexes = [
            models.Index(fields=['data_inicio', 'data_fim']),
            models.Index(fields=['valor_parcial']),
        ]