from django.db import models
from .disciplinas import Disciplina

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)