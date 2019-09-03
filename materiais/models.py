from django.db import models

# Create your models here.

class Unidade(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Material(models.Model):
    descricao = models.CharField(max_length=100)
    valorUnitario = models.DecimalField(max_digits=7, decimal_places=2)
    consumivel = models.CharField(max_length=10)
    observacoes = models.TextField()
    estoqueMinimo = models.DecimalField(max_digits=7, decimal_places=2)
    estoqueMaximo = models.DecimalField(max_digits=7, decimal_places=2)
    estoqueAtual = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='materiais_imagens' ,null=True, blank=True)
    idUnidade = models.ForeignKey(Unidade,null=True, blank=True, on_delete=models.PROTECT)
    idCategoria = models.ForeignKey(Categoria,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
