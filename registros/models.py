from django.db import models
from cruds.models import Fornecedor
from cruds.models import Requisitante

# Create your models here.

class PedidoCompra(models.Model):
    dataRegistro = models.DateField()
    dataRecebimento = models.DateField()
    valorTotal = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField()
    idFornecedor = models.ForeignKey(Fornecedor,null=False, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.dataRegistro

class RecepcaoMateriais(models.Model):
    dataRegistro = models.DateField()
    notaFiscal = models.CharField(max_length=50)
    valorTotal = models.DecimalField(max_digits=7, decimal_places=2)
    idPedidoCompra = models.ForeignKey(PedidoCompra,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.notaFiscal

class RequisicaoMateriais(models.Model):
    dataRegistro = models.DateField()
    condicao = models.CharField(max_length=10)
    observacoes = models.TextField()
    idRequisitante = models.ForeignKey(Requisitante,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.condicao

class RetiradasMateriais(models.Model):
    dataRegistro = models.DateField()
    horaRegistro = models.TimeField()
    situacao = models.CharField(max_length=10)
    idRequisicaoMateriais = models.ForeignKey(RequisicaoMateriais,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.situacao

class DevolucaoMateriais(models.Model):
    dataRegistro = models.DateField()
    horaRegistro = models.TimeField()
    situacao = models.CharField(max_length=10)
    observacoes = models.TextField()
    idRetiradasMateriais = models.ForeignKey(RetiradasMateriais,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.situacao
