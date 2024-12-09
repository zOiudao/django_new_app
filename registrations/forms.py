from django import forms
from . import models

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = models.Empresa
        fields = '__all__'