from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'password',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome de usuário', 'type': 'text', 'name': 'login_user'}
            ),
            'password': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Senha', 'type': 'text', 'name': 'login_pass'}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este email já está cadastrado!', code='invalid')
            )
            return email