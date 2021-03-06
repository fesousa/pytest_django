from django.db import models
from .disciplinas import Disciplina
from django.utils.functional import cached_property


class Pessoa(models.Model):
    
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=9)
    ra = models.IntegerField()

    @cached_property
    def sobrenome(self):
        return self.nome.split(' ')[-1]

    def retornaCargaHoraria(self):
        return "Método não implementado"

    # definir como classe abstrata para não criar tabela
    class Meta:
        abstract = True