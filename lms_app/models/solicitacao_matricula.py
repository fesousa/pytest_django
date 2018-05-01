from django.db import models
from .alunos import Aluno
from .disciplinas_ofertadas import DisciplinaOfertada

class SolicitacaoMatricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.CASCADE)