from django.db import models

class Files(models.Model):

    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=6)
    valor = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=15)
    hora = models.CharField(max_length=6)
    dono = models.CharField(max_length=50)
    loja = models.CharField(max_length=150)