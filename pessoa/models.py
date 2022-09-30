from django.db import models

# Create your models here.


class Pessoa(models.Model):

    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ativo = models.BooleanField(default=True)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)
