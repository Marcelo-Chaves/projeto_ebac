from django.shortcuts import render
from .models import Pessoa
# Create your views here.

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request,'app_ebac/listar_pessoas.html', {'pessoas':pessoas})

