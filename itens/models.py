from django.db import models
from registros.models import PedidoCompra, RecepcaoMateriais, RequisicaoMateriais, RetiradasMateriais, DevolucaoMateriais
from materiais.models import Material

# Create your models here.

class itemRecepcao(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.DecimalField(max_digits=7, decimal_places=2)
    subTotal = models.DecimalField(max_digits=7, decimal_places=2)
    idRececaoMateriais = models.ForeignKey(RecepcaoMateriais,null=True, blank=True, on_delete=models.PROTECT)
    idMaterial = models.ForeignKey(Material,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor

class itemPedidoCompra(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.DecimalField(max_digits=7, decimal_places=2)
    subTotal = models.DecimalField(max_digits=7, decimal_places=2)
    idPedidoCompra = models.ForeignKey(PedidoCompra,null=True, blank=True, on_delete=models.PROTECT)
    idMaterial = models.ForeignKey(Material,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor

class itemRequisicao(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.DecimalField(max_digits=7, decimal_places=2)
    idRequisicaoMateriais = models.ForeignKey(RequisicaoMateriais,null=True, blank=True, on_delete=models.PROTECT)
    idMaterial = models.ForeignKey(Material,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor

class itemRetirada(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.DecimalField(max_digits=7, decimal_places=2)
    idRetiradasMateriais = models.ForeignKey(RetiradasMateriais,null=True, blank=True, on_delete=models.PROTECT)
    idMaterial = models.ForeignKey(Material,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor

class itemDevolucao(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.DecimalField(max_digits=7, decimal_places=2)
    idDevolucaoMateriais = models.ForeignKey(DevolucaoMateriais,null=True, blank=True, on_delete=models.PROTECT)
    idMaterial = models.ForeignKey(Material,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.valor
