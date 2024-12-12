from django.db import models
from django.utils import timezone

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateTimeField(default=timezone.now) 

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    funcional = models.CharField(max_length=15)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now) 

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"

    def __str__(self):
        return self.nome
    

class Chave(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return self.nome



