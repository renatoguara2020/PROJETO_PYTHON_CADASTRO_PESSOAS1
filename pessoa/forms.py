from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'email', 'ativo',
                  'data_nascimento', 'data_cadastro']
