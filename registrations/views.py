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
            return redirect('index')
    else:
        form = forms.EmpresaForm()
    return render(request, 'partials/empresa_form.html', {'form': form})



