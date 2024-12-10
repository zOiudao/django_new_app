from django import forms
from . import models

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = models.Empresa
        fields = 'nome',
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa'}),
        }