from django.db import models
from .pessoas import Pessoa
from .disciplinas import Disciplina

class Aluno(Pessoa):
    desconto = models.FloatField()
    #mensalidade = models.FloatField()
    disciplinas = models.ManyToManyField(Disciplina)

    def add_desconto(self, porcentagem):
        self.desconto = self.desconto + porcentagem
    
    def rm_desconto(self, porcentagem):
        self.desconto = self.desconto - porcentagem

    def get_mensalidade(self):
        soma_mensalidade = 0
        for d in self.disciplinas.all():
            soma_mensalidade += d.valor
        return soma_mensalidade * (1 - self.desconto/100)

    def get_carga_horaria(self):
        soma_carga = 0
        for d in self.disciplinas.all():
            soma_carga += d.carga_horaria
        return soma_carga