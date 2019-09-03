from django.db import models

# Create your models here.

class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.municipio

class Telefone(models.Model):
    ddd = models.CharField(max_length=5)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero

class Fornecedor(models.Model):
    razaoSocial = models.CharField(max_length=50)
    nomeFantasia = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dataRegistro = models.DateField()
    observacoes = models.TextField()
    idEndereco = models.ForeignKey(Endereco,null=True, blank=True, on_delete=models.PROTECT)
    idTelefone = models.ForeignKey(Telefone,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.razaoSocial

class Departamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Requisitante(models.Model):
    nome = models.CharField(max_length=50)
    observacoes = models.TextField()
    idDepartamento = models.ForeignKey(Departamento,null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
