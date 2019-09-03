from django.db import models
#from almoxarifado.cruds.models import Requisitante
# Create your models here.

class RequisicaoMateriais(models.Model):
    dataRegistro = models.DateField()
    condicao = models.CharField(max_length=10)
    observacoes = models.TextField()
    #idRequisitante = models.ForeignKey(Requisitante,null=True, blank=True, on_delete=models.PROTECT)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.condicao
