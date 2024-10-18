from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome



class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)
    idade = models.IntegerField()
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_funcionario