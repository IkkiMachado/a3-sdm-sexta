from django.db import models
from django.core.validators import MinValueValidator

class Acessorio(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco_adicional = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0.00,
        help_text="Preço adicional por dia quando este acessório é incluído no veículo"
    )
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} (+R${self.preco_adicional}/dia)"

    class Meta:
        verbose_name = "Acessório"
        verbose_name_plural = "Acessórios"
        ordering = ['nome']