from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.nome} ({self.matricula})'

