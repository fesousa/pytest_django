from django.db import models
from .pessoas import Pessoa
from .disciplinas import Disciplina

class Professor(Pessoa):
   
    ''' sem composicao
    '''
    # carga_horaria = models.IntegerField()   

    # def add_carga_horaria(self, horas):
    #     self.carga_horaria = self.carga_horaria + horas
    
    # def rm_carga_horaria(self, horas):
    #     self.carga_horaria = self.carga_horaria - horas

    ''' com composicao
    '''

    disciplinas = models.ManyToManyField(Disciplina)

    def add_disciplina(self, disciplina):
        self.disciplinas.add(disciplina)

    def calcula_carga_horaria(self):
        soma_carga = 0
        for d in self.disciplinas:
            soma_carga += d.carga_horaria
        return soma_carga
