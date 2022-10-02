from django.db import models
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
from datetime import datetime
# Create your models here.


class Pessoa(models.Model):

    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ativo = models.BooleanField(default=True)
    data_nascimento = models.DateField(null=True)
    data_cadastro = models.DateTimeField(default=datetime.now())


def __str__(self) -> str:
    self.nome_completo
