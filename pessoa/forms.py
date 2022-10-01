from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        models = Pessoa
        fields = ['nome_completo', 'ativo' 'email',
                  'data_nascimento', 'data_cadastro']
