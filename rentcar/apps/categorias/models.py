from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    valor_base = models.DecimalField('Valor Base', max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome