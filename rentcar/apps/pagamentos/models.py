from django.db import models
from django.core.validators import MinValueValidator
from reservas.models import Reserva

class Pagamento(models.Model):
    class MetodoPagamento(models.TextChoices):
        CARTAO = 'CARTAO', 'Cartão de Crédito/Débito'
        PIX = 'PIX', 'PIX'
        BOLETO = 'BOLETO', 'Boleto Bancário'

    class StatusPagamento(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        APROVADO = 'APROVADO', 'Aprovado'
        RECUSADO = 'RECUSADO', 'Recusado'

    reserva = models.OneToOneField(
        Reserva,
        on_delete=models.PROTECT,
        related_name='pagamento',
        verbose_name='Reserva associada'
    )
    valor_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name='Valor total do pagamento'
    )
    metodo = models.CharField(
        max_length=10,
        choices=MetodoPagamento.choices,
        verbose_name='Método de pagamento'
    )
    status = models.CharField(
        max_length=10,
        choices=StatusPagamento.choices,
        default=StatusPagamento.PENDENTE,
        verbose_name='Status do pagamento'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    dados_transacao = models.JSONField(
        blank=True,
        null=True,
        verbose_name='Dados da transação (gateway de pagamento)'
    )

    def __str__(self):
        return f"Pagamento #{self.id} - {self.get_status_display()} ({self.valor_total})"

    @property
    def is_aprovado(self):
        return self.status == self.StatusPagamento.APROVADO

    def aprovar(self):
        """Marca o pagamento como aprovado"""
        self.status = self.StatusPagamento.APROVADO
        self.save()

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-data_criacao']
