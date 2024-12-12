from django.contrib import messages
from django.shortcuts import render, redirect
from registrations import forms, models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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
        exibir_empresas = models.Empresa.objects.all()
    return render(request, 'partials/empresa_form.html', {'form': form, "exibir_empresas": exibir_empresas})


def add_funcionario(request):
    form = forms.FuncionarioForm()
    if request.method == 'POST':
        form = forms.FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('funcionario')
    else:
        form = forms.FuncionarioForm()
    return render(request, 'partials/funcionario_form.html', {'form': form})


def add_chave(request):
    if request.method == 'POST':
        key_name = request.POST.get('key_name')
        key_number = request.POST.get('key_number')
        cdt_key = models.Chave(nome=key_name, numero=key_number)
        cdt_key.save()
        return redirect('funcionario')
    
    return render(request, 'partials/chave_form.html')


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Login invalido')

    return render(request, "partials/login.html", {'form': form})