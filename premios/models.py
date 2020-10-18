from django.db import models

class Premio(models.Model):
    nome = models.CharField(max_length = 120)
    sigla = models.CharField(max_length = 5)
    descricao = models.TextField()
    