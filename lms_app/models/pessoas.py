from django.db import models

class Pessoa(models.Model):
    
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=9)
    ra = models.IntegerField()

    def get_sobrenome(self):
        return self.nome.split(' ')[-1]

    # definir como classe abstrata para não criar tabela
    class Meta:
        abstract = True