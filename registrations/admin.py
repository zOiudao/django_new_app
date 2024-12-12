from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Chave)
class ChaveAdmin(admin.ModelAdmin):
    ...