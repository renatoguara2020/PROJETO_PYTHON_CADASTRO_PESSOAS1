from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Pessoa
from .forms import PessoaForm
# Create your views here.


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('id')


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa'
