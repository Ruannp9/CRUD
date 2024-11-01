from django.db import models

# Create your models here.
class Time_Futebol(models.Model):
    
    nome_time = models.CharField(max_length=200)
    tecnico_time = models.CharField(max_length=200)
    data_criacao = models.DateField()
    Mascote = models.CharField(max_length=200)
    quantidade_titulos = models.IntegerField()

    def __str__(self):
        return self.nome_time