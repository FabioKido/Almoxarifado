from django.db import models

# Create your models here.

class Material(models.Model):
    descricao = models.CharField(max_length=100)
    valorUnitario = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='materiais_imagens' ,null=True, blank=True)

    def __str__(self):
        return self.descricao
