from django.contrib import messages
from django.shortcuts import render, redirect
from registrations import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_empresa(request):
    if request.method == 'POST':
        form = forms.EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('empresa')
    else:
        form = forms.EmpresaForm()
    return render(request, 'partials/empresa_form.html', {'form': form})


def add_funcionario(request):
    if request.method == 'POST':
        form = forms.FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('funcionario')
    else:
        form = forms.FuncionarioForm()
    return render(request, 'partials/funcionario_form.html', {'form': form})