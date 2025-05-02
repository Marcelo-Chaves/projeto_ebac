from django.contrib import admin
from .models import Pessoa
# Register your models here.

@admin.register(Pessoa)
class Pessoaadmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']


