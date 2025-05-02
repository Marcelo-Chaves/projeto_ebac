import pytest
from django.core.exceptions import ValidationError
from app_ebac.models import Pessoa

@pytest.mark.django_db
def test_criar_pessoa():
    pessoa = Pessoa.objects.create(nome="Jackeline", email="jackeline@example.com", telefone="123456789")
    assert Pessoa.objects.count() == 1
    assert pessoa.nome == "Jackeline"
    assert pessoa.email == "jackeline@example.com"
    assert pessoa.telefone == "123456789"

@pytest.mark.django_db
def test_criar_pessoa_marcelo():
    pessoa = Pessoa.objects.create(nome="Marcelo", email="marcelo@example.com", telefone="123456789")
    assert Pessoa.objects.count() == 1
    assert pessoa.nome == "Marcelo"
    assert pessoa.email == "marcelo@example.com"
    assert pessoa.telefone == "123456789"