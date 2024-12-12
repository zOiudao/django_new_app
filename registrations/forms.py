from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = models.Empresa
        fields = 'nome',


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = models.Funcionario
        fields = ("nome", "sobrenome", "funcional", "empresa",)
        widgets = {
            "nome": forms.TextInput(
                attrs={
                'class': 'form-control',
                "placeholder": 'Nome'
            }),
            "sobrenome": forms.TextInput(
                attrs={
                'class': 'form-control',
                "placeholder": 'Sobrenome'
            }),
            "funcional": forms.TextInput(
                attrs={
                'class': 'form-control',
                "placeholder": 'Funcional'
            }),
            "empresa": forms.Select(
                attrs={
                'class': 'form-control',
                'selected': 'selecione a empresa'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = "" 


class RegisterForm(UserCreationForm):
    ...