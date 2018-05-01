from django.db import models
from .pessoas import Pessoa


class Aluno(Pessoa):
    desconto = models.FloatField()
    #mensalidade = models.FloatField()

    def adicionaDesconto(self, porcentagem):
        self.desconto = self.desconto + porcentagem
    
    def removeDesconto(self, porcentagem):
        self.desconto = self.desconto - porcentagem

    def retornaValorMensalidade(self):
        soma_mensalidade = 0
        for d in self.disciplinas.all():
            soma_mensalidade += d.valor
        return soma_mensalidade * (1 - self.desconto/100)

    def retornaCargaHoraria(self):
        soma_carga = 0
        # procurar disciplinas do aluno
        
        from .solicitacao_matricula import SolicitacaoMatricula
        solicitacoes = SolicitacaoMatricula.objects.filter(aluno=self.id)

        for s in solicitacoes:
            soma_carga += s.disciplina_ofertada.disciplina.carga_horaria        
        
        return soma_carga
        # for d in self.disciplinas.all():
        #     soma_carga += d.carga_horaria
        # return soma_carga