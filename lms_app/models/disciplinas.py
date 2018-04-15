from django.db import models
from .cursos import Curso
from ..managers import DisciplinaManager

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    valor = models.FloatField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ativo =models.BooleanField(default=True)

    objects = DisciplinaManager()

    @property
    def cursoNome(self):
        return self.curso.nome