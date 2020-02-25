from django.db import models

class CoreFilmes(models.Model):
    nome = models.CharField(max_length=40)
    mes = models.CharField(max_length=10)
    ano = models.IntegerField()
    genero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    receita = models.FloatField()

    class Meta:
        managed = False
        db_table = 'core_filmes'
